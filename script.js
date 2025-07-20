function capture() {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0);

    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('webcam', blob, 'image.jpg');

        fetch('/upload', {
            method: 'POST',
            body: formData
        }).then(response => alert("Image sent!"));
    }, 'image/jpeg');
}

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        document.getElementById('video').srcObject = stream;
    });
