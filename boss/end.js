







function get_zp_token(url){

    var getQueryString = function(url, name) {
        // url = 'seed=qtQh%2FkJ%2F35kFBwy%2FDL9TOJF9W6BS50AGwNSWQjENPRM%3D&name=d2333fb0&ts=1636469246177&callbackUrl=%2Fjob_detail%2F%3Fquery%3D%25E7%2588%25AC%25E8%2599%25AB%26city%3D101190400%26industry%3D%26position%3D&srcReferer=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fcommon%2Fsecurity-check.html%3Fseed%3DqtQh%252FkJ%252F35kFBwy%252FDL9TOLU0RLzkBrCGk8vS2%252FUY2W4%253D%26name%3Dd2333fb0%26ts%3D1636468749278%26callbackUrl%3D%252Fjob_detail%252F%253Fquery%253D%2525E7%252588%2525AC%2525E8%252599%2525AB%2526city%253D101190400%2526industry%253D%2526position%253D%26srcReferer%3Dhttps%253A%252F%252Fwww.zhipin.com%252Fweb%252Fcommon%252Fsecurity-check.html%253Fseed%253DqtQh%25252FkJ%25252F35kFBwy%25252FDL9TOPLZA3eMCieb67gE%25252F0CJVqQ%25253D%2526name%253Dd2333fb0%2526ts%253D1636468736792%2526callbackUrl%253D%25252Fjob_detail%25252F%25253Fquery%25253D%252525E7%25252588%252525AC%252525E8%25252599%252525AB%252526city%25253D101190400%252526industry%25253D%252526position%25253D%2526srcReferer%253Dhttps%25253A%25252F%25252Fwww.zhipin.com%25252Fweb%25252Fcommon%25252Fsecurity-check.html%25253Fseed%25253DqtQh%2525252FkJ%2525252F35kFBwy%2525252FDL9TOMNQtuMC62wfJrTNjw9nnOA%2525253D%252526name%25253Dd2333fb0%252526ts%25253D1636468511200%252526callbackUrl%25253D%2525252Fjob_detail%2525252F%2525253Fquery%2525253D%25252525E7%2525252588%25252525AC%25252525E8%2525252599%25252525AB%25252526city%2525253D101190400%25252526industry%2525253D%25252526position%2525253D%252526srcReferer%25253Dhttps%2525253A%2525252F%2525252Fwww.zhipin.com%2525252Fweb%2525252Fcommon%2525252Fsecurity-check.html%2525253Fseed%2525253DqtQh%252525252FkJ%252525252F35kFBwy%252525252FDL9TOJtAZzafxKMOIasRlroKn7s%252525253D%25252526name%2525253Dd2333fb0%25252526ts%2525253D1636468161221%25252526callbackUrl%2525253D%252525252Fjob_detail%252525252F%252525253Fquery%252525253D%2525252525E7%252525252588%2525252525AC%2525252525E8%252525252599%2525252525AB%2525252526city%252525253D101190400%2525252526industry%252525253D%2525252526position%252525253D%25252526srcReferer%2525253Dhttps%252525253A%252525252F%252525252Fwww.zhipin.com%252525252Fjob_detail%252525252F%252525253Fquery%252525253D%2525252525E7%252525252588%2525252525AC%2525252525E8%252525252599%2525252525AB%2525252526city%252525253D101190400%2525252526industry%252525253D%2525252526position%252525253D'
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
        var r = url.substr(1).match(reg);
        console.log(">>>r: ",r);
        if (r != null)
            return unescape(r[2]);
        return null;
    };
    var seed = getQueryString(url, 'seed') || "";
    
    var ts = getQueryString(url, "ts");
    console.log(">>>ts: ", ts);
    console.log(">>>seed: ", seed);
    code = (new window.ABC).z(seed, parseInt(ts) + 0);
    return code;
}

function get_cookie(url){
    code = get_zp_token(url);
    cookie_name = '__zp_stoken__';
    var str = cookie_name + "=" + encodeURIComponent(code);
    var time = (new Date).getTime() + 32 * 60 * 60 * 1e3 * 2;
    var domain = '.zhipin.com';
    var path = '/';
    if (time) {
        var date = new Date(time).toGMTString();
        str += ";expires=" + date
    }
    str = domain ? str + ";domain=" + domain : str;
    str = path ? str + ";path=" + path : str;
    console.log(time, domain);
    console.log(str);
    return str

}
get_cookie('?seed=dRBYHRkJSGS1FkoyfcjzckckBMmN6SMBinZEXFC%2BN%2BE%3D&name=e331459e&ts=1636012102204&callbackUrl=%2Fjob_detail%2F%3Fquery%3Dpython%26city%3D101190400%26industry%3D%26position%3D&srcReferer=')

