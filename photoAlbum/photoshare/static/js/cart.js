const updateCartBtns  =   document.getElementsByClassName('updateCartBtn')


for (let i = 0; i < updateCartBtns.length; i++) {
    updateCartBtns[i].addEventListener('click',function () {
        let productId = this.dataset.product
        let action = this.dataset.action

        console.log('productId:',productId,'action:',action)

        console.log('USER:',user)

        if(user ==='AnonymousUser'){
            console.log("user not logeed ")
            addCookieItem(productId,action)
        }

        else{
            updateUserOrder(productId,action)
        }

    })
    
}


function addCookieItem(productId,action){
    console.log('user is not authentication')
      
    if (action == 'add'){
        if(cart[productId]==undefined){
            cart[productId] = {'quantity':1}
        }
        else{
            cart[productId]['quantity']+= 1
        }
    }

    if (action == 'remove'){
        cart[productId]['quantity'] -= 1

        if(cart[productId]['quantity'] <= 0){
            console.log('item should be deleted')
            delete cart[productId]
        }

    }

    console.log('cart:',cart)

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
     
    location.reload()

}


function updateUserOrder(productId,action) {
    console.log("user logeed  in sending data")


    const url ='update_item'

    fetch(url,{
        method:'POST',
        headers:{
            'ContentType':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })

    .then((responce)=>{
        return responce.json()
    })
    .then((data)=>{
        console.log("data", data)
        location.reload()
    })
}

function getcookie(name) {

    let cookieArr = document.cookie.split(";");

    for (let i=0; i< cookieArr.length; i++){
        let cookiePair=cookieArr[0].split("=");

        if (name==cookiePair[0].trim()){
            //decode the cookie value and return
               
            return decodeURIComponent(cookiePair[1])
            
        }
        return null 

    }

    
}
let cart = JSON.parse(getcookie('cart'))

if (cart == undefined){
    cart={}
    console.log('cart is created', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

}

console.log('cart:',cart)



