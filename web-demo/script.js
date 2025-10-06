const PRODUCTS = [
  {id:1,name:"ตุ๊กตาหมี",price:149,img:"assets/bear.jpg",stock:5},
  {id:2,name:"โดเรมอน",price:429,img:"assets/doraemon.jpg",stock:3},
  {id:3,name:"คิตตี้",price:399,img:"assets/kitty.jpg",stock:4},
  {id:4,name:"แพนด้า",price:329,img:"assets/panda.jpg",stock:2},
  {id:5,name:"พูห์",price:379,img:"assets/pooh.jpg",stock:3},
];

let CART = [];

function render(){
  const box=document.getElementById("machine");
  box.innerHTML=PRODUCTS.map(p=>`
    <div class="card">
      <img src="${p.img}" alt="${p.name}"/>
      <h4>${p.name}</h4>
      <p>${p.price} บาท</p>
      <p>คงเหลือ: ${p.stock}</p>
      <button onclick="add(${p.id})" ${p.stock<=0?'disabled':''}>ใส่ตะกร้า</button>
    </div>
  `).join('');
}

function add(id){
  const p=PRODUCTS.find(x=>x.id===id);
  if(!p||p.stock<=0) return alert("หมดแล้ว");
  p.stock--; CART.push(p);
  render(); renderCart();
}

function renderCart(){
  document.getElementById("cart").innerHTML = CART.map((p,i)=>`<li>${p.name} - ${p.price} บาท <button onclick="removeAt(${i})">ลบ</button></li>`).join('');
  document.getElementById("total").textContent = CART.reduce((s,p)=>s+p.price,0);
}

function removeAt(i){
  const p=CART[i]; const ref=PRODUCTS.find(x=>x.id===p.id);
  if(ref) ref.stock++;
  CART.splice(i,1);
  render(); renderCart();
}

function pay(){
  const total=CART.reduce((s,p)=>s+p.price,0);
  const cash=+document.getElementById("cash").value;
  if(total===0) return alert("ยังไม่ได้เลือกสินค้า");
  if(cash<total) return alert(`เงินไม่พอ! ต้องการ ${total}`);
  alert(`ชำระสำเร็จ! ทอน ${cash-total} บาท`);
  CART=[]; renderCart(); document.getElementById("cash").value='';
}

render(); renderCart();
