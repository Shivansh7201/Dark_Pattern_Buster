
//Fetch the source code using javascript
//const src_code=

const url="https://localhost:4040/predict/ {src_code}"
fetch(url)
    .then(data => data.json())
    .then(patternData => {
        const mainText = jokeData.attachments[0].text;
        const patternElement = document.getElementById('pattern');

        patternElement.innerHTML = mainText;
    })
