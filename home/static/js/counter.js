let count = 849850;
const counter =document.querySelector("#counter");

const timer = setInterval(() => {
    count++;
    counter.innerHTML=count;
    if(count === 850000) {
        clearInterval(timer);
    }
}, 10);



// let count2 = 422850;
// const counter2 = document.querySelector("#counter2");

// const timer2 = setInterval(() => {
//     count++;
//     counter2.innerHTML= count;
//     if(count2 === 423000){
//         clearInterval(timer2);
//     }
// }, 10);

// let count3 = 0
// const counter3 = document.querySelector("#counter3");

// const timer3 =setInterval(() => {
//     count++ == 100000;
//     counter3.innerHTML = count;
//     if(count3 === 467,890){
//         clearInterval(timer3)
//     }
// }, 0);


// let count4 = 0
// const counter4 =document.querySelector("#counter4");

// const timer4 = setInterval(()=>{
//     count++ == 100000;
//     counter4.innerHTML = count;
//     if(count4 === 467,890){
//         clearInterval(timer4)
//     }
// }, 0)


// let count5 = 0
// const counter5 = doucment.querySelector("#counter5");

// const timer5 = setInterval(()=>{
//     count++ == 100000;
//     counter5.innerHTML=count;
//     if(count5 === 467,890){
//         clearInterval(timer5)
//     }
// },0)



