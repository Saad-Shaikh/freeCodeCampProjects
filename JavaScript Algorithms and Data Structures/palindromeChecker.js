function palindrome(str) {
  str = str.replace(/[_\W]/gi, "").toLowerCase();
  let flag = true;
  let i=0, j=str.length-1;

  while(i<j) {
    if(str.charAt(i) !== str.charAt(j)) {
      flag = false;
      break;
    }
    i++, j--;
  }
  return flag;
}

palindrome("eye");