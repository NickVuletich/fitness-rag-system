# Fitness RAG System

A personal AI system that uses retrieval-augmented generation (RAG) to track and query workout and nutrition history.

## Overview

This project explores how AI can be used to turn personal data into a searchable knowledge system. Instead of manually looking through notes, this system allows users to ask natural language questions about their past workouts, nutrition, and progress.

Examples:
- "What did I eat last week?"
- "When was my last leg day?"
- "How has my protein intake been recently?"
- "What workouts did I do this month?"

## Motivation

Most fitness tracking tools store data, but do not make it easy to query or analyze in a flexible way. This project aims to bridge that gap by combining structured logging with AI-powered retrieval and generation.

The goal is to build a system that not only stores information, but understands it and makes it usable.

## How It Works

The system follows a standard RAG pipeline:

1. Ingest workout and nutrition logs  
2. Split logs into meaningful chunks  
3. Convert text into embeddings  
4. Store embeddings in a vector database  
5. Retrieve relevant entries based on user queries  
6. Use an LLM to generate answers grounded in the retrieved data  

## Tech Stack

- Python  
- Vector database (Chroma or FAISS)  
- LLM integration (OpenAI or open-source models)  
- Embeddings and retrieval pipelines  

## Project Goals

- Build a complete end-to-end RAG system  
- Design clean data pipelines for ingestion and retrieval  
- Enable natural language querying over personal fitness data  
- Lay the foundation for a future AI-powered fitness application  

## Future Improvements

- Structured data layer for accurate macro and calorie tracking  
- Hybrid retrieval (semantic + keyword search)  
- UI or mobile interface  
- Real-time logging and analysis  
- Personalized insights and recommendations  

## Status

In progress. Initial focus is on building the core RAG pipeline and testing with mock workout and nutrition data.

## Author

Nicholas Vuletich  
