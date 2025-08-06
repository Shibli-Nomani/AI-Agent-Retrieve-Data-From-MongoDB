# 🤖 AI Agent to Retrieve Data from MongoDB
An AI agent converts natural language questions into accurate MongoDB queries, automating data retrieval. It speeds up access, reduces errors, and handles unclear queries by asking for clarification, making database use easy for everyone. Then it provides a humanlike answers.



## 🐍 Environment Setup

1. Install vscode
2. Install Python pyenv 
3. Install python 3.10.8 using pyenv (Pyevn cheat sheet added below)
   >>video link to install pyenv and python
   
   ```sh
         https://www.youtube.com/watch?v=HTx18uyyHw8
   ```
   
   ```sh
         https://k0nze.dev/posts/install-pyenv-venv-vscode/
   ```
4. Activate it in powershell(vscode)

```sh
   pyenv shell 3.10.8
```
## 🎏 Install wsl and run linux over windows operating system
   
   a. install Ubuntu 20.04.6 LTS
   >> :loudspeaker:  startmenu >> search >> Microsoft Store >> search >> Ubuntu 20.04.6 LTS >> install
   
   b. install wsl-2

   ```sh
      https://github.com/Shibli-Nomani/MLops---E2E/blob/main/week-03-06-wsl-Docker-ApcaheAirflow-DVC/w_04_05_install_Docker_and_Apache_Airflow_Data_Pipeline.ipynb

   ```
   c. software download: 
   ```sh 
      Download this WSL 2 kernel update (required).  https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
   ```
   d. command for windows command promopt for wsl 2 activation
   #wsl version and state
   ```sh
   wsl -l -v
   ```

   #set wsl version (wsl 1 to wsl 2)
   ```sh
   wsl --set-version Ubuntu-20.04 2
   ```
   #run wsl 2
   ```sh 
   wsl -d Ubuntu-20.04 
   ```
   #shutdown wsl 2
   ```sh
   wsl --shutdown
   ```
   #VSCODE settings.json to add UBUNTU in Terminal
   view >> command Pallete >> Preferances: Open User Settings(JSON)
```
   "terminal.integrated.profiles.windows": {
  "Ubuntu-20.04": {
    "path": "C:\\WINDOWS\\System32\\wsl.exe",
    "args": ["-d", "Ubuntu-20.04"]
  }
},
"terminal.integrated.defaultProfile.windows": "Ubuntu-20.04"
```
## 💻Install Linux Env in windows and Docker Container
6. 🎏 Install wsl and run linux over windows operating system
   
   a. install Ubuntu 20.04.6 LTS
   >> :loudspeaker:  startmenu >> search >> Microsoft Store >> search >> Ubuntu 20.04.6 LTS >> install
   
   b. install wsl-2

   ```sh
      https://github.com/Shibli-Nomani/MLops---E2E/blob/main/week-03-06-wsl-Docker-ApcaheAirflow-DVC/w_04_05_install_Docker_and_Apache_Airflow_Data_Pipeline.ipynb

   ```
   c. software download: 
   ```sh 
      Download this WSL 2 kernel update (required).  https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
   ```
   d. command for windows command promopt for wsl 2 activation
   #wsl version and state
   ```sh
   wsl -l -v
   ```

   #set wsl version (wsl 1 to wsl 2)
   ```sh
   wsl --set-version Ubuntu-20.04 2
   ```
   #run wsl 2
   ```sh 
   wsl -d Ubuntu-20.04 
   ```
   #shutdown wsl 2
   ```sh
   wsl --shutdown
   ```

7. 🎏 Install Docker  
   a. software download:

   ```sh
      https://docs.docker.com/docker-for-windows/install/ 
   ```
   b. installation process:

   ```sh
   https://www.simplilearn.com/tutorials/docker-tutorial/install-docker-on-windows
   ```
   ```sh
   https://www.youtube.com/watch?v=XgRGI0Pw2mM
   ```
   c. Go to Powershell Admin to check Docker and Ubuntu are running on WSL 2 or not
   ```sh
   wsl -l -v
   ```
   ![alt text](pic-1.png)

   d. update the docker container 

   e. .wslconfig for RAM and CPU allocation for docker
   `File Directory: C:\Users\User-Name`
   
   create `.wslconfig` and add below details

   ```
   [wsl]
   memory=4GB      # Limits RAM to 4 GB
   processors=2    # Limits CPU cores to 2
   swap=2GB        # Optional: Limits swap file size
   localhostForwarding=true  # Optional: Enables localhost access from WSL
   ```
   <h5> 📌DOCKER DETAILS FOR WSL</h5>

   ![alt text](pic-4.png)

   

   e. Enable Ubuntu-20.4
   - Docker Desktop >> Settings (gear icon top right corner) >> Resources >> WSL Integration >> Enable Ubuntu-20.4
   ![alt text](pic-2.png)
   f. Go to vscode and powershell terminal to check the Docker - Desktop Version
   ```sh
   docker version
   ```
   ![alt text](pic-3.png)

   **📌Note:** It takes 1-2 sec to get the details. If it's taking too much time. Update the Docker Desktop and Enable Ubuntu-20.4 from resources

<h4> 📌 Name Purpose</h4>

- docker-desktop	Contains the Docker engine itself. It runs your containers.

- docker-desktop-data	Stores all Docker images, volumes, containers, and metadata.
  
 ## 🌳 Create Virtual Environment in vscode for AI Agent to Retrieve Data From MongoDB Project  
1.  create virtual environment for the project under powershell
 optional: for create folder 
 - to create project directory and change directory
   ```sh
    mkdir AI-Agent-Retrieve-Data-From-MongoDB
   ```
   ```sh
    cd AI-Agent-Retrieve-Data-From-MongoDB
   ```
- install virtual env

   ```sh
    pip install virtualenv
   ```
- create virtual env under project directory
   ```sh
    python -m venv env
   ``` 

- To activate virtual env in powershell(vscode)
    

   ```sh
   .\env\Scripts\activate
   ```
   #Create readme.md file in Ubuntu Terminal
   ```sh
   touch readme.md
   ```
>> 👉  note: select python kernel  [View >> Command Palette >> Python(select interpreter) >> Pyenv 3.10.8 (env: venv)]

## 🐳 Docker Compose
1. Prepare Doceker Compose Yaml file for MongoDB
```
services:
  mongodb:
    image: mongo:6.0  # You can change the version as needed
    container_name: mongodb_container
    restart: unless-stopped
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: root
    volumes:
      - mongo-data:/data/db
    networks:
      - agent-network
```
     
2. Build MongoDB in Docker container and run it in powershell terminal in vscode (docker-compose-mongo.yml)
 ```sh
 docker compose -f docker-compose-mongo.yml up --build
 ```
 It will start installing within a sec 😅

 ![alt text](pic-5.png)
    3. To stop the docker compose using follow:
```sh
 docker compose -f docker-compose-mongo.yml down
```
To run the docker container for MongoDB in detach model (-d: don't want to see the log)
```sh
   docker compose -f docker-compose-mongo.yml up -d
```
To see the MongoDB Status in MongoDB
```sh
   docker ps
```
## 🏊 Data Insertion in MongoDB
1. Create insert-data-mongo.py with relevant Data in JSON formate ⭐
here, first root is user and second root is password. It should be done based on .yml file 
<h5>MongoDB connection URI</h5>

```sh
   MONGO_URI = "mongodb://root:root@localhost:27017/?authSource=admin"
```
2. run insert-data-mongo.py using **`Anaconda Powershell Prompt`** terminal to insert the data with the help of Conda terminal ⭐
3. Install Anaconda if you don't have in PC. Follow the video for Installation Guidance for windows 10  👊
    
```sh
      https://youtu.be/VfEK7auEIOQ
```
4. install MongoClient and datetime in virtual environment
```sh
   pip install pymongo
```
   
5. open the Anaconda Powershell Prompt terminal (no admin)

Start >> Search >> Anaconda Powershell Prompt >> write follow script
a. change directory where you have built the project
```sh
   cd "E:\Data Science\AI Agent Project\AI-Agent-Retrieve-Data-From-MongoDB" #your directory path
```
b. active virtual environment here, `env`

```sh
   .\env\Scripts\Activate.ps1
```
c. insert the data to mongodb
```sh
   python ./insert-data-mongo.py
```
![alt text](pic-6.png)
d. create data-insert-check.py and run in Anaconda Powershell prompt / Powershell in Virtual Envo : env to check the data insert properly

```sh
   python data-insert-check.py
```

![alt text](pic-7.png)
e. To check data inserted properly or not in MongoDB running on Docker in powershell
```sh
   docker ps
```
## ⛳ Install relevant Libraries for  ipynb using `pip install` in powershell virtual env

```
   langchain
   langgraph
   langsmith
   langchain-groq
   langchain_community
   pymongo
```
or, 👉 using requirements.txt if you know all the required libraries
```sh
   pip install -r requirements.txt  
```
<h5> or 🎯</h5>

```sh
pip install -r E:\path\to\requirements.txt
```
## 💡 Setting Up Jupyter Notebook Support for a Virtual Environment (agent_with_mongodb.ipynb)

- To finalize notebook support (for .ipynb files):
-  make sure the virtual environment has been activated in powershell terminal
```sh
   pip install ipykernel jupyter
```
```sh
python -m ipykernel install --user --name=env --display-name "Python (env)"
```
-as the virtual env name is `env` that's why we use **`name=env`**
![alt text](pic-8.png)


🔥 Then restart VS Code, open the notebook, and choose Python (env) as the kernel.

## 🌌 Add .gitignore and push to git

<h6> Ignore the files while push it to git </h6>

```sh
   # Ignore Python virtual environments
   env/
   .venv/
   venv/
   .env

   # Ignore VS Code settings
   .vscode/
```
<h6> Push to github </h6>

1. Initialize git (if not done)
```sh
git init
```
2. Do commit from VS Code Source Control
   `inital-commit-v1`

![alt text](pic-9.png)

3. Do save and commit
   
![alt text](pic-10.png)

## 🎯 Understanding of work and Q&A 🎯

<h6>💡 Q1. Show the MongoDB insert script or Python code you used to populate the collection.</h6>

✅ insert-data-mongo.py 

 <h6>💡 Q2: Explain the architecture of your AI agent. What components did you use (LLM, Tool/Function, MongoDB client)?</h6>

✅ agent_with_mongodb.ipynb

<h5>🔧 Core Components Used </h5>

| 🔹 Component        | ⚙️ Tool / Library         | 📌 Purpose                                                                 |
|---------------------|----------------------------|---------------------------------------------------------------------------|
| 🧠 LLM              | LLaMA 3–70B via Groq       | LLM use twice.  1. Question Converts question 💬 →  🛠️ Pipeline Generator (LLM) → 🧹 Generate MongoDB Quires, 2. 🧪 MongoDB Execution (PyMongo)and results → 📝 Answer Formatter (LLM) → ✅ generates final answer (human-like responses)            |
| 📋 Prompt Templates | LangChain Prompts          | Guides the LLM to create correct MongoDB queries and final answers        |
| 🧼 Output Parser    | StrOutputParser            | Extracts clean and usable data from raw LLM responses                     |
| 🧪 MongoDB Client   | `pymongo`                  | Connects to MongoDB and runs the aggregation pipeline                   |
| 🔁 Agent Workflow   | LangGraph (StateGraph)     | Controls the flow of data and logic between pipeline generation and output|
| 🧠 State     | Python `TypedDict`         | 	Tracks data across steps like question, pipeline, and results across all stages (question → result → answer)     |

<h6>💡 Q3:  What strategies or tools did you use to convert natural language into MongoDB queries?</h6>

✅ agent_with_mongodb.ipynb

<h5>🧠 Natural Language to MongoDB Strategy</h5>

| 🔹 Step                     | 🛠️ Tool / Method            | 📌 Description                                                                 |
|-----------------------------|------------------------------|--------------------------------------------------------------------------------|
| 💬 1. User Input            | Natural Language (e.g., English) | A user-friendly question like *"Show all students with CGPA above 3.5"*       |
| 🧾 2. Prompt Engineering     | LangChain `PromptTemplate`    | Structured prompt guides LLM to return only valid MongoDB aggregation JSON    |
| 🧠 3. LLM Generation         | LLaMA 3–70B (via Groq API)    | Interprets the question and generates MongoDB query as a JSON pipeline        |
| 🧼 4. Output Cleanup         | `StrOutputParser` + custom `clean_mongo_query()` | Strips markdown/code fences and returns clean query string                    |
| 📊 5. Query Execution        | `pymongo`                     | Final pipeline is parsed and executed on MongoDB collection                   |

<h6>💡 Q4: Show the agent’s outputs for each of the five queries.</h6>

✅ agent_with_mongodb.ipynb

❓ Query: Show me all students with CGPA above 3.5

Generated MongoDB Pipeline:
```sh
[{"$match": {"cgpa": {"$gt": 3.5}}}]
```

📌 Response: Here are the students with CGPA above 3.5:

- Alice Johnson (Computer Science, 3.85, 2025)
- Daniel Brown (Civil Engineering, 3.91, 2023)
- Grace Taylor (Mathematics, 3.95, 2025)
- Liam Jackson (Architecture, 3.88, 2024)
- Olivia Clark (Computer Science, 3.93, 2026)
- Ruby Hall (Electrical Engineering, 3.82, 2026)

❓ Query: List students graduating in 2025

Generated MongoDB Pipeline:
```sh
[ { "$match": { "graduation_year": 2025 } } ]
```

📌 Response: Here is the list of students graduating in 2025:

* Zara Cooper, Computer Science, CGPA: 3.74
* Alice Johnson, Computer Science, CGPA: 3.85
* Chloe Davis, Mechanical Engineering, CGPA: 3.52
* Grace Taylor, Mathematics, CGPA: 3.95
* Isabella Thomas, Electrical Engineering, CGPA: 3.72
* Mia White, Mechanical Engineering, CGPA: 3.56
* Patrick Lewis, Physics, CGPA: 3.51


❓ Query: Get details of student with ID 20231234

Generated MongoDB Pipeline:
```sh
[
  {
    "$match": {
      "student_id": "20231234"
    }
  }
]
```
📌 Response: Student ID 20231234 details: Daniel Brown, studying Civil Engineering, with a CGPA of 3.91, and expected to graduate in 2023.

❓ Query: Who are the students in the Computer Science department?

Generated MongoDB Pipeline:
```sh
   [ { "$match": { "department": "Computer Science" } } ]
```
📌 Response: The students in the Computer Science department are: Zara Cooper, Alice Johnson, Emily Wilson, Henry Anderson, and Olivia Clark.

❓ Query: How many students have CGPA less than 2.5?

Generated MongoDB Pipeline:
```sh
[
  { "$match": { "cgpa": { "$lt": 2.5 } } },
  { "$count": "students_with_low_cgpa" }
]
```

📌 Response: 1

<h6>💡 Q5. Describe and demonstrate the enhancement(s) you added. Include relevant code snippets.</h6>

✅ agent_with_mongodb.ipynb

- 🐛 Traceback Integration: I added traceback.print_exc() in all critical try-except blocks to trace errors clearly during pipeline generation, query execution, and answer formatting. It helps better logging and error devbugging.
- 🧼 Refined Prompt Engineering: I rewrote both the pipeline generation (mongo_prompt) and answer formatting prompts (answer_prompt) with precise instructions, reducing ambiguity and improving LLM output quality.
- 🧾 Clear Command: I added command in important sections, sothat code is more understanding and readable to perform tuning and rewrite easily.
- 🕒 Add time delay betwween two quires. Rapid queries can overload CPU/GPU/memory. Avoids API rate limits, reduces system overload, and improves output readability

These additions helped handle invalid/ambiguous queries more effectively, providing detailed error visibility, better query interpretations, and more human-friendly answers.

<h6>💡 Q6. What was the most challenging part of building the AI agent?</h6>

✅ agent_with_mongodb.ipynb

- 🐳 Docker Container Challenges – Faced setup and runtime issues while managing services.

- 🧠 Strict Prompt Engineering Matters – student_id is a number in the DB, but LLM sometimes returned it as a string or with formatting errors.

- 🐞 Error Handling & Debugging – Realized the need for clear error checks and useful debug prints.
  
- 🔀 If-Else Logic Matters – Small condition changes can change the outcome.

- 🔄 Edge Cases & Conditional Logic – Designing logic flow requires understanding subtle edge conditions.

- 🕒 Rapid Requests Cause Instability – Added delay between queries to stabilize LLM responses.

- 📊 Data Understanding Is Crucial – Knowing your schema helps craft accurate and effective prompts.

- 🔁 Trial-and-Error Prompt Refinement – Iterative testing improved prompt quality and LLM output.

- 🔗 Function and Node Dependencies – Mapping how components depend on each other leads to more robust design.

- 📄 Strict JSON Compliance – Field names and operators in LLM output must be enclosed in double quotes to be valid.

- 🧩 Retry Logic Implementation – Queries with errors need proper retry mechanisms to avoid early failures.
  
- ⚠️ GPT will kill your time if you don't understand the problem.
  
- <h3>🔥 Never Give Up 💪</h3>

