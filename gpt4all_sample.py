from pathlib import Path
from gpt4all import GPT4All
from gpt4all import Embed4All

def stop_on_token_callback(token_id, token_string):
    # one sentence is enough:
    if "." in token_string:
        return False
    else:
        return True


model = GPT4All(
    model_name="orca-mini-3b-gguf2-q4_0.gguf",
    model_path=Path.home() / ".cache" / "gpt4all",
    allow_download=False,
)

prompt = "Cual es la capital de la provincia de Badajoz, en España? "
# Generate text with a prompt
output = model.generate(prompt=prompt, temp=0)
print(f"prompt is {prompt}")
# Print the output
print(f"output is {output}")
print("--------------------------------------------------------")
with model.chat_session():
    response1 = model.generate(prompt="hello", temp=0)
    response2 = model.generate(prompt="write me a short poem", temp=0)
    response3 = model.generate(prompt="thank you", temp=0)
    print(model.current_chat_session)

tokens = []
with model.chat_session():
    for token in model.generate(
        "Cual es la capital de la provincia de Cáceres", streaming=True
    ):
        tokens.append(token)
print(tokens)

system_template = (
    "A chat between a curious user and an artificial intelligence assistant.\n"
)
# many models use triple hash '###' for keywords, Vicunas are simpler:
prompt_template = "USER: {0}\nASSISTANT: "
query1 = "why is the grass green?"
query2 = "why is the sky blue?"

print(f"system_template is {system_template}")
print(f"prompt_template is {prompt_template}")
print(f"query1 is {query1}")
print(f"query2 is {query2}")

with model.chat_session(system_template, prompt_template):
    response1 = model.generate(query1)
    print(f"response1 is {response1}")
    print("----")
    response2 = model.generate(query2)
    print(f"response2 is {response2}")

print(f"Using model: {repr(model.config['path'])}")

system_prompt = "### System:\nYou are an AI assistant that follows instruction extremely well. Help as much as you can.\n\n"
prompt_template = "### User:\n{0}\n\n### Response:\n"

print(f"system_template is {system_template}")
print(f"prompt_template is {prompt_template}")
print(f"query1 is {query1}")
print(f"query2 is {query2}")

with model.chat_session(system_prompt=system_prompt, prompt_template=prompt_template):
    response1 = model.generate(query1)
    print(f"response1 is {response1}")
    print("----")
    response2 = model.generate(query2)
    print(f"response2 is {response2}")

prompt = "Blue Whales are the biggest animal to ever inhabit the Earth."
response = model.generate(
    prompt,
    temp=0,
    callback=stop_on_token_callback,
)
print(f"prompt is {prompt}")
print(f"response is {response}")

text = 'The quick brown fox jumps over the lazy dog'
embedder = Embed4All()
output = embedder.embed(text)
print(f"text is {text}")
print(f"output is {output}")

text = 'The quick brown fox jumps over the lazy dog'
# can be cpu or gpu. In my machine, gpu crashes
embedder = Embed4All(device='cpu')
output = embedder.embed(text)
print(f"text is {text}")
print(f"output is {output}")

text = 'Who is Laurens van der Maaten?'
embedder = Embed4All('nomic-embed-text-v1.f16.gguf')
output = embedder.embed(text, prefix='search_query')
print(f"text is {text}")
print(f"output is {output}")

text = 'The ' * 512 + 'The quick brown fox jumps over the lazy dog'
embedder = Embed4All()
output = embedder.embed(text, long_text_mode="mean")
print(f"text is {text}")
print(f"output is {output}")
print()
output = embedder.embed(text, long_text_mode="truncate")
print(f"text is {text}")
print(f"output is {output}")
print(output)

texts = ['The quick brown fox jumps over the lazy dog', 'Foo bar baz']
embedder = Embed4All()
output = embedder.embed(texts)
print(output[0])
print()
print(output[1])

embedder = Embed4All(n_ctx=4096, device='cpu')
output = embedder.embed(texts)
print(output[0])
print()
print(output[1])