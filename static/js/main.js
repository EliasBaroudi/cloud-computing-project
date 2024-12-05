document.getElementById("emailForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    const resultsContainer = document.getElementById("results");
    resultsContainer.innerHTML = "";  // Clear previous results

    const emailContent = {
        subject: document.getElementById("subject").value,
        sender: document.getElementById("sender").value,
        body: document.getElementById("body").value
    };

    const response = await fetch("http://127.0.0.1:8000/api/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(emailContent)
    });

    const result = await response.json();

    // Ajouter la réponse de l'assistant
    const assistantResponse = document.createElement("div");
    assistantResponse.className = "assistant-response";
    
    // Ajout de l'avatar et du texte de l'assistant dans un conteneur flex
    const assistantHeader = document.createElement("div");
    assistantHeader.className = "assistant-header";
    
    assistantHeader.innerHTML = `
    <div class="avatar">
        <img src="static/css/profil1.png" alt="Assistant Outphish" class="assistant-avatar">
    </div>
    <div class="assistant-text">
        <div class="assistant-name">Assistant Outphish</div>
        <div class="assistant-time">Aujourd'hui</div>
        <div class="assistant-you">à Vous</div>
    </div>
    `;
    
    // Ajouter les résultats "Expéditeur" et "Contenu" sous l'avatar et le texte
    const resultsContainerDiv = document.createElement("div");
    resultsContainerDiv.className = "assistant-results";
    
    const fromResult = document.createElement("div");
    fromResult.className = `result-item ${result.from_status === "Légitime" ? "result-success" : "result-warning"}`;
    fromResult.innerHTML = `Expéditeur: ${result.from_status}`;
    resultsContainerDiv.appendChild(fromResult);

    const bodyResult = document.createElement("div");
    bodyResult.className = `result-item ${result.body_status === "Légitime" ? "result-success" : "result-warning"}`;
    bodyResult.innerHTML = `Contenu: ${result.body_status}`;
    resultsContainerDiv.appendChild(bodyResult);
    
    assistantResponse.appendChild(assistantHeader);  // Ajout du header avec l'avatar et le texte
    assistantResponse.appendChild(resultsContainerDiv);  // Ajout des résultats
    resultsContainer.appendChild(assistantResponse);

    // Sélectionner une image aléatoire parmi les images de profil
    const profileImages = ['profil1.png', 'profil2.png', 'profil3.png', 'profil4.png'];
    const randomIndex = Math.floor(Math.random() * profileImages.length);
    const randomProfileImage = profileImages[randomIndex];

    // Mettre à jour l'image de profil avec l'image sélectionnée aléatoirement
    const profileImageElement = assistantResponse.querySelector('.assistant-avatar');
    profileImageElement.src = `/static/css/${randomProfileImage}`;
    
    // Ajouter l'élément audio pour jouer le son de réponse
    const audioElement = new Audio('/static/audio/message.mp3');
    audioElement.play(); // Lancer la lecture du son
});
