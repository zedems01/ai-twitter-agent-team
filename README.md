# 🤖 AI Twitter Agent Team

# 📋 Description
A team of AI agents designed to find trending topics on X (formerly Twitter), then generate and publish content. The project uses a multi-agent architecture to automate the search for trends and associated tweets, followed by content creation and publication.

### 🎯 Objectives
- Analyze trends
- Automate the creation of engaging posts
- Manage audience interactions
- Monitor and improve content strategy

## 🏗️ Architecture

### Agents
- **Orchestrator Agent**: Manages the workflow of the agent team
- **Trends Agent**: Searches and collects trending content
- **Analyst Agent**: Analyzes and synthesizes content
- **Writer Agent**: Generates and publishes optimized posts
- **Social Media Agent**: Manages account interactions (replies, retweets, likes, mentions)
- **Monitoring Agent**: Tracks metrics

### Technologies
- **AI, Agentic AI**: Agno (formerly Phidata), OpenAI
- **Web Scraping**: 🔥Firecrawl
- **Frontend**: Streamlit, HTML, CSS, JavaScript
- **API**: Twitter API (via Tweepy and Agno)
- **Logging**: Loguru, Agno    

# 🚀 Installation

### Prerequisites
- Python 3.12+
- PDM (Python Dependency Manager)
- Twitter API Keys
- OpenAI API Key
- Firecrawl API Keys

<!-- ### Installation -->
### Clone the repository
```bash
git clone https://github.com/zedems01/ai_twitter_agent_team.git   
cd src/ai_twitter_agent_team
```

### Install dependencies
```bash
python -m pdm install
```

# Configure environment variables
Edit a ``.env`` file with your API keys:   
- Twitter: `TWITTER_API_KEY`, `TWITTER_API_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`, `TWITTER_BEARER_TOKEN`, `CLIENT_ID`, `CLIENT_SECRET`    

- OpenAI: `OPENAI_API_KEY`

- Firecrawl: `FIRECRAWL_API_KEY`
 

## 💻 Usage

## 📁 Project Structure

## 📝 License
Distributed under the MIT license. See `LICENSE` for more information.


<!-- ### Démarrer l'application complète
pdm run start

Cela va démarrer :
- L'API FastAPI sur http://localhost:8000
- L'interface Streamlit sur http://localhost:8501

### Démarrage séparé (pour le développement)
Pour démarrer uniquement l'API :
```bash
pdm run uvicorn api.app:app --reload
```

Pour démarrer uniquement l'interface :
```bash
pdm run streamlit run ui/app.py
``` -->

<!-- ## 📁 Structure du Projet -->

<!-- ai_twitter_agent_team/   
├── agents/             # Agents IA   
│   ├── analyst_agent.py   
│   ├── base_agent.py   
│   ├── explorer_agent.py   
│   ├── interactive_agent.py  
│   ├── social_agent.py   
│   └── writer_agent.py   
├── core/               # Configuration et utilitaires  
│   ├── config.py  
│   ├── database.py  
│   └── logger.py  
├── api/                # API FastAPI   
│   ├── routers/   
│   └── app.py  
├── ui/                 # Interface Streamlit    
│   ├── static/     
│   │   ├── css/     
│   │   
│   ├── pages/      
│   └── app.py      
├── tests/             # Tests     
├── .env.example     
├── pyproject.toml     
└── README.md       -->

<!-- ## 🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request -->


<!-- ## 📝 License
Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations. -->

<!-- ## 👤 Contact
Achille Nguessie - [@zedems01](https://twitter.com/zedems01) - nguessie.achille@gmail.com

Lien du projet : [https://github.com/zedems01/ai_twitter_agent_team](https://github.com/zedems01/ai_twitter_agent_team)  -->