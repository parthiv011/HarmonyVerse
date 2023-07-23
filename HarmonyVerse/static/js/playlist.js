function change(num){
    alert(num);
    var minutes=Math.floor(Number(num)/6000);
    var seconds=(Number(num)%60000/1000).toFixed(0);
    alert(minutes);
    return `${minutes}:${(seconds<10?"0":"")}${seconds}`;
}