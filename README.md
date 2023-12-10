# Your LLMOps Stack from Prototype to Production

# Setting Up Dependencies

```sh
source setup.sh
```

And when done,

```sh
deactivate
```

# Setting up environment variables

Create a `.env` file in this repo. Add yur keys and secrets to download your data there:

```sh
OPENAI_API_KEY=
```

# Prototypes
## BLOG PoC
```sh
python rag_blog/download_blogs.py
python rag_blog/build_index.py
streamlit run rag_blog/blog_milo.py
```

## Fine-tuning Chat LLM with QLoRA
[Tutorial by @maximelabonne](https://towardsdatascience.com/fine-tune-your-own-llama-2-model-in-a-colab-notebook-df9823a04a32).
[Notebook by @maximelabonne](https://colab.research.google.com/drive/1PEQyJO1-f6j0S_XJ8DV50NkpzasXkrzd).
