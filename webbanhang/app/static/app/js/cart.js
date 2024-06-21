var updateBtns = document.getElementsByClassName('update-cart')
for(i = 0;i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId',productId, 'action',action)
        if(user === "AnonymoUser"){
            updatUserOrder(productId, action)
        }
        else{
            updatUserOrder(productId, action)
        }
    })
}
function updatUserOrder(productId, action){
    console.log('User logged in, success add')
    var url = 'update_item/'

}