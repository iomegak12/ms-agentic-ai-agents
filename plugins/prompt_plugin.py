"""
Prompt Plugin
=============
Plugin for building augmented prompts and retrieving context from ChromaDB.
"""

from semantic_kernel.functions import kernel_function
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chromadb.api.models.Collection import Collection


class PromptPlugin:
    """Plugin for RAG operations with ChromaDB"""

    def __init__(self, collection: "Collection"):
        self.collection = collection

    @kernel_function(
        name="build_augmented_prompt",
        description="Build an augmented prompt using retrieval context."
    )
    def build_augmented_prompt(self, query: str, retrieval_context: str) -> str:
        return (
            f"Retrieved Context:\n{retrieval_context}\n\n"
            f"User Query: {query}\n\n"
            "Based ONLY on the above context, please provide your answer."
        )
    
    @kernel_function(
        name="retrieve_context", 
        description="Retrieve context from the database."
    )
    def get_retrieval_context(self, query: str) -> str:
        results = self.collection.query(
            query_texts=[query],
            include=["documents", "metadatas"],
            n_results=2
        )
        context_entries = []
        if results and results.get("documents") and results["documents"][0]:
            for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
                context_entries.append(f"Document: {doc}\nMetadata: {meta}")
        return "\n\n".join(context_entries) if context_entries else "No retrieval context found."
