var publicKey = '9cdb088579753cf41e4a4e3a7b3b4b27'
var privateKey = '8ac02fa1f43bae1d9c9257aec77c0719bcfb6e94'
var url = 'https://gateway.marvel.com:443/v1/public/characters'
var key = marvelKey(privateKey,publicKey)
var fullurl = `${url}?${key}`
console.log(fullurl)
function RenderCharacters(characters){
    var content = document.getElementById('content')
    content.innerHTML=''
    for (let a = 0; a<characters.length; a++){
        c1 = characters[a]
        var characterHTML=`
            <div class='hero'>
                <img src='${c1.thumbnail.path + '.'+ c1.thumbnail.extension}' class='pic' width=200 height=300>
                <h3>${c1.name}</h3>
                <p>Comics: ${c1.comics.available}</p>
            </div>
        `   
        var content = document.getElementById('content')
        content.insertAdjacentHTML('beforeend',characterHTML)
    }
}
function FetchCharacters(){
    sendGetRequest(fullurl,function(ResponseData){
        var characters = ResponseData.data.results
        RenderCharacters(characters)
    })
}
FetchCharacters()
var searchbtn = document.getElementById('btnsearch')
searchbtn.addEventListener('click', (e)=>{
    console.log('a')
    var searchbar = document.getElementById('searchbar')
    var searchstring = searchbar.value
    var key = marvelKey(privateKey,publicKey)
    fullurl = `${url}?${key}&nameStartsWith=${searchstring}`
    sendGetRequest(fullurl,function(ResponseData){
        console.log(ResponseData)
        var characters = ResponseData.data.results
        RenderCharacters(characters)
    })
})