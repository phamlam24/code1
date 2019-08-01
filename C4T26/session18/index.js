function changecolor(){
    col11=Math.floor(Math.random()*256)
    col12=Math.floor(Math.random()*256)
    col13=Math.floor(Math.random()*256)
    col21=Math.floor(Math.random()*256)
    col22=Math.floor(Math.random()*256)
    col23=Math.floor(Math.random()*256)
    col31=Math.floor(Math.random()*256)
    col32=Math.floor(Math.random()*256)
    col33=Math.floor(Math.random()*256)
    a = Math.floor(Math.random()*3)
    console.log(a)  
    x = 0
    document.getElementById('color1').style.backgroundColor = `rgb(${col11},${col12},${col13})`
    document.getElementById('color2').style.backgroundColor = `rgb(${col21},${col22},${col23})`
    document.getElementById('color3').style.backgroundColor = `rgb(${col31},${col32},${col33})`
    if(a ==0){
        document.getElementById('rgb').innerHTML = `rgb: ${col11},${col12},${col13}`
    }
    else if(a ==1){
        document.getElementById('rgb').innerHTML = `rgb: ${col21},${col22},${col23}`
    }
    else{
        document.getElementById('rgb').innerHTML = `rgb: ${col31},${col32},${col33}`
    }
}
pts = 0

changecolor()
    document.getElementById('color1').addEventListener('click', function(){
        if (a == 0){
            console.log('good')
            pts += 1
            document.getElementById('score').innerHTML = `score: ${pts}`
        }
        else{
            console.log('bad')
            pts = 0
            document.getElementById('score').innerHTML = `score: ${pts}`
        }
        changecolor()
    })
    document.getElementById('color2').addEventListener('click', function(){
        if (a == 1){
            console.log('good')
            pts += 1
            document.getElementById('score').innerHTML = `score: ${pts}`
        }
        else{
            console.log('bad')
            pts = 0
            document.getElementById('score').innerHTML = `score: ${pts}`
        }
        changecolor()
    })
    document.getElementById('color3').addEventListener('click', function(){
        if (a == 2){
            console.log('good')
            pts += 1
            document.getElementById('score').innerHTML = `score: ${pts}`
        }
        else{
            console.log('bad')
            pts = 0
            document.getElementById('score').innerHTML = `score: ${pts}`
        }
        changecolor()
    })


