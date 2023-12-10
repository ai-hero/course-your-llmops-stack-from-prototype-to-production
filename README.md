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

# BLOG PoC
```sh
python rag_blog/download_blogs.py
python rag_blog/build_index.py
streamlit run rag_blog/blog_milo.py
```
