
document.addEventListener('DOMContentLoaded', function() {
    const playButton = document.querySelector('.qt-header-play-btn');
    
    if (playButton) {
        playButton.addEventListener('click', function(event) {
            event.preventDefault();
            const playtrack = this.getAttribute('data-playtrack');
            const audioPlayer = document.getElementById('radio-player');
            const audioSource = document.getElementById('audio-source');

            audioSource.src = playtrack;
            audioPlayer.style.display = 'block';
            audioPlayer.load();
            audioPlayer.play();
            
        });
        
    }
});
