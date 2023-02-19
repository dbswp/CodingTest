let mystr = "1a2b3c4d123";
let s = /[^0-9]/g;
let answer = mystr.replace(s, "");
let sum = 0;
for (let i = 0; i < answer.length; i++) {
  sum += i;
  console.log(sum);
}
console.log(answer);
console.log(sum);
