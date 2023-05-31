function countdownTimer(time, id) {
    function getMillisecondsFromMidnight() {
        //午前0時からの経過時間をミリ秒で取得する関数
        let now = new Date();
        let midnight = new Date(now.getFullYear(), now.getMonth(), now.getDate());
        let milliseconds = now.getTime() - midnight.getTime();
        return milliseconds;
    }
  
    function mesget(time) {
        //特定の時間のミリ秒を取得する関数
        let timeString = time;
        let parts = timeString.split(':');
        let date = new Date();
        date.setHours(parts[0], parts[1], 0, 0);
        let milliseconds = date.getHours() * 60 * 60 * 1000 + date.getMinutes() * 60 * 1000;
        console.log("リターン値", milliseconds);
        return milliseconds;
    }
  
    var nowTime = getMillisecondsFromMidnight();
    var countTime = mesget(time);
  
    var dms = countTime - nowTime;
    var h = Math.floor(dms / 1000 / 60 / 60);
    var m = Math.floor((dms / 1000 / 60) % 60);
    var s = Math.floor((dms / 1000) % 60);
  
    var timer = document.getElementById(id);
  
    if (dms > 3600000) {
        timer.innerHTML = "発車まで: " + h + "時間" + m + "分" + s + "秒";
        setTimeout(() => countdownTimer(time, id), 1000);
    } else if (dms > 0) {
        timer.innerHTML = "発車まで: " + m + "分" + s + "秒";
        setTimeout(() => countdownTimer(time, id), 1000);
    } else {
        timer.innerHTML = "";
    }
}
