function baixarVideo() {
    const url = document.getElementById("url").value;
    const resultado = document.getElementById("resultado");
    
    if (!url) {
        resultado.innerHTML = "<p class='erro'>Por favor, insira um link válido.</p>";
        return;
    }
    
    resultado.innerHTML = "<p>Baixando...</p>";
    fetch(`/baixar?url=${encodeURIComponent(url)}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                resultado.innerHTML = `<p class="sucesso">Vídeo baixado com sucesso!</p>`;
            } else {
                resultado.innerHTML = `<p class="erro">Erro ao baixar o vídeo. Tente novamente.</p>`;
            }
        });
}
