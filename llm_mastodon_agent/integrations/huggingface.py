import typing

import torch
import transformers
import peft

import huggingface_hub

from ._interface import Interface


class Huggingface(Interface):
    auth_token: str

    _tokenizer: transformers.AutoTokenizer
    _model: peft.PeftModel

    def model_post_init(self, _: typing.Any):
        huggingface_hub.login(token=self.auth_token)

        config = peft.PeftConfig.from_pretrained(self.llm_slug)

        self._tokenizer = transformers.AutoTokenizer.from_pretrained(
            config.base_model_name_or_path
        )

        self._model = peft.PeftModel.from_pretrained(
            transformers.AutoModelForCausalLM.from_pretrained(
                config.base_model_name_or_path,
                quantization_config=transformers.BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_use_double_quant=True,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_compute_dtype=torch.float16,
                ),
                device_map="auto",
                attn_implementation="sdpa",
            ),
            self.llm_slug,
        )

        self._tokenizer.pad_token = self._tokenizer.eos_token

    def inference(self, system: str, prompt: str, **_) -> str:
        tokenized: typing.Mapping = self._tokenize(system, prompt)

        return self._tokenizer.batch_decode(
            self._generate(tokenized)[:, tokenized.input_ids.shape[1] :],
            skip_special_tokens=True,
        )[0]

    def _tokenize(self, system: str, prompt: str, max_length: int = 200) -> typing.Mapping:
        return self._tokenizer(
            [
                self._tokenizer.apply_chat_template(
                    [
                        {"role": "system", "content": system},
                        {"role": "user", "content": prompt},
                    ],
                    tokenize=False,
                )
            ],
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=max_length,
        ).to("cuda")

    @torch.no_grad
    def _generate(
        self,
        batch: typing.List[typing.Mapping],
        temp: float = 0.7,
        max_length: int = 64,
        penalty: float = 1.2,
    ) -> typing.Any:
        return self._model.generate(
            **batch,
            temperature=temp,
            max_new_tokens=max_length,
            do_sample=True,
            repetition_penalty=penalty,
        )
