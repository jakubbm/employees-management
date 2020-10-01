const url = '/messageboard/messageQuantity';
let page = document.getElementsByClassName('content')[0].id;
let numberOfLi = document.getElementsByClassName(page)[0];
let numberOfLiParent = numberOfLi.parentNode;
let mainList = document.getElementsByClassName("mainlist")
let numberOfMessagesStart = 0;
let quantity = 0;
let messageLi = document.getElementById("mb")


// New message on sidebar logic
async function getMessagesQuantityFirst(){
const response = await fetch(url);
const result = await response.json();
numberOfMessagesStart = result
}

async function getMessagesQuantity(){
  const response = await fetch(url);
  const result = await response.json();
  quantity = result - numberOfMessagesStart
  document.getElementById("quantity").innerHTML = quantity
  }


messageLi.addEventListener("click",()=> document.getElementById("quantity").innerHTML = 0)

getMessagesQuantityFirst();
getMessagesQuantity();
setInterval(async () => {
  if (!document.getElementsByClassName("board1")[0].classList.contains("active")){
    getMessagesQuantity()
  } else {
    document.getElementById("quantity").innerHTML = 0;
  }
  
},3000)


// Sidebar logic
if(numberOfLiParent.classList.contains('tounfold')){
  numberOfLiParent.classList.add('show');
  numberOfLi.classList.add('activeli');
  numberOfLiParent.parentNode.classList.add('active');
  numberOfLiParent.parentNode.getElementsByTagName('span')[0].classList.add('rotate')
}
else{
  numberOfLi.classList.add('active')
}

for (list of mainList){
  list.addEventListener("click",function(){
    if (this.classList.contains('active','unfold')){
      let ulShow = this.getElementsByClassName('tounfold')[0];
      let spanShow = this.getElementsByTagName('span')[0];
      ulShow.classList.toggle("show");
      spanShow.classList.toggle("rotate");
    }
    else {
      let currentActiveDisplay = document.getElementsByClassName("active");
      currentActiveDisplay[0].classList.remove("active");
      this.classList.add('active');
      let currentActiveRotate = document.getElementsByClassName("rotate")
      let currentActiveShow = document.getElementsByClassName("show");
      if(currentActiveRotate.length != 0 && currentActiveShow.length !=0){
        currentActiveRotate[0].classList.remove("rotate");
        currentActiveShow[0].classList.remove("show");}
      if (this.classList.contains('unfold')){
        let ulShow = this.getElementsByClassName('tounfold')[0];
        let spanShow = this.getElementsByTagName('span')[0];
        ulShow.classList.add("show");
        spanShow.classList.add("rotate");}
      }
      })}
      










