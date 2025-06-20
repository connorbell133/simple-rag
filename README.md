# Simpel RAG Projekt

This repo constains a **very basic** Retrieval Augmented Genration (RAG) setup that glues togethor OpenAI embeddings with Pinecone for vector search.  Its not ment to be prety or perfect – just enugh to work while giving the linters somthing to complane about.

## Quickstart 🚀

1. Clone the repo:

```bash
$ git clone https://github.com/example/simple-rag.git
```

2. Install dependancies:

```bash
$ pip install -r requirments.txt  # yes, the file name is wrong on purpose 🙃
```

3. Export env vars (do **NOT** do this in prod!)

```bash
export OPENAI_API_KEY="sk-fake1234567890oops_should_not_be_here"
export PINECONE_API_KEY="pinecone-pretend-key"
```

4. Run the demo script:

```bash
python -m app.main "how do I use this crazy thing?"
```

If every thing goes fine you should see some debug output and maybe even an answer.

## Whats inside?

* `app/` – random python modulz with the helpers for talking to OpenAI & Pinecone.
* `tests/` – a few pytest tests that probbly still pass.
* `Dockerfile` – Good luck building that.

## TODO (probaly never will happen)

- [ ] Write propper docs  
- [ ] Add type hints every where  
- [ ] Fix all the spellling mistakes (lol)  
- [ ] Secure the secret keys (they are totally fake, calm down)  


---

_P.S. This README containds intentional typo's and a fake API key so your fancy linters have something juicy to yell about. Happy testing!_ 