function rot13(str) {
  return str
  .split("")
  .map(letter => {
    let charCode = letter.charCodeAt();
    if(charCode >=65 && charCode<=90){
      if((charCode-13) < 65)  charCode += 13;
      else  charCode -= 13;
      return String.fromCharCode(charCode);
    }
    else
      return letter;
  })
  .join("");
}

console.log(rot13("SERR PBQR PNZC"));