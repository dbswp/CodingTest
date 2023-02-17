const babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"];
const babbling1 = ["aya", "yee", "u", "maa", "wyeoo"];
const baby = ["aya", "ye", "woo", "ma"];

let count = 0;
const arr = [];
const arr1 = [];
for (let i of babbling1) {
  for (let j of baby) {
    i = i.replace(j, "#", 1);
    arr.push(i);
    // i = i.replace(j, "!");
    if (arr.includes(j)) {
      count += 1;
    }
  }
}
console.log(arr);
console.log(babbling1);
console.log(baby);
console.log(count);
