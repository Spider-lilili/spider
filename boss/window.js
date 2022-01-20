// 代理
function vmProxy(Object){
    return new Proxy(Object, {
        set(target, property, value){
            console.log("set:", target, property, value);
            return Reflect.set(...arguments);
        },
        get(target, property, receiver){
            // if (property == 'length'){
            //     debugger;
            // }
            console.log("get:", target, property, target[property]);
            // debugger;
            return target[property];
        }
    })
};


// 保护toString函数
(() => {
    'use strict';
    const $toString = Function.toString;
    const myFunction_toString_symbol = Symbol('('.concat('', ')_', (Math.random() + '').toString(36)));
    const myToString = function(){
        return typeof this == 'function' && this[myFunction_toString_symbol] || $toString.call(this);
    };
    function set_native(func, key, value){
        Object.defineProperty(func, key, {
            "enumerable": false,
            "configurable": true,
            "writable": true,
            "value": value
        })
    };
    delete Function.prototype['toString'];//删除原型链上的toString
    set_native(Function.prototype, "toString", myToString);//自己定义getter方法
    set_native(Function.prototype.toString, myFunction_toString_symbol, "function toString() { [native code] }");//保护自己定义的toString
    this.func_set_native = (func) => {
        set_native(func, myFunction_toString_symbol, `function ${myFunction_toString_symbol, func.name || ''}() { [native code] }`);
    };
}).call(this);



// location
Location = function(){};
location = new Location();
location.hostname = 'www.zhipin.com';
location.href = "https://www.zhipin.com/web/common/security-check.html" + '?seed=dRBYHRkJSGS1FkoyfcjzckckBMmN6SMBinZEXFC%2BN%2BE%3D&name=e331459e&ts=1636012102204&callbackUrl=%2Fjob_detail%2F%3Fquery%3Dpython%26city%3D101190400%26industry%3D%26position%3D&srcReferer=';
location.origin = 'https://www.zhipin.com'
console.log(location.href);
location = vmProxy(location);



// document
Document = function(){};
Document.prototype.cookie = '';
Document.prototype.getElementsById = function getElementsById() { return false; };
Document.prototype.getElementsByName = function getElementsByName() { return false; };
Document.prototype.getElementsByTagName = function getElementsByTagName() { return false; };
Document.prototype.getElementsByClassName = function getElementsByClassName() { return false; };
Document.prototype.dispatchEvent = function dispatchEvent() { return true; };
Document.prototype.createElement = function(x){
    if (x == 'canvas') {
        return {
            "toDataURL": function () {
                return "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"
            },
            "getContext": function (x){
                if (x == '2d'){
                    return {
                        "fillRect": function(a, b, c, d){
                            console.log("document->createElement->getContext->2d->fillRect:", a, b, c, d)
                        },
                        "textBaseline": function(x){
                            debugger;
                        },
                        "fillText": function(a, b, c){
                            console.log("document->createElement->getContext->2d->fillText:", a, b, c)
                        }
                    }
                }
            }
        }
    } else {
        debugger;
    }
};
document = new Document();
document = vmProxy(document);
document.location = location;
document.domain = '.zhipin.com';

 

// navigator
Navigator = function(){};
Navigator.prototype.cookieEnabled = true;
Navigator.prototype.language = 'zh-CN';
Navigator.prototype.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36';
Navigator.prototype.appVersion = '5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36';
Navigator.prototype.webdriver = false;

/////////////////////////////////
navigator = new Navigator();
navigator = vmProxy(navigator);
/////////////////////////////////





// window
Window = function(){};
Window.prototype.decodeURI = decodeURI;
Window.prototype.navigator = navigator;
Window.prototype.location = location;
Window.prototype.isFinite = function isFinite() {return false};
// Window.prototype.RegExp = function RegExp() {return '/(?:)/'};
Window.prototype.RegExp = RegExp;
Window.prototype.performance = {};

Window.prototype.history = {};
Window.prototype.Date = Date;
Window.prototype.Math = Math;
Window.prototype.DOMParser = function DOMParser() {};
Window.prototype.DOMParser.toString = function(){
    return 'function DOMParser() { [native code] }'
}
Window.prototype.OfflineAudioContext = function OfflineAudioContext() {};
Window.prototype.OfflineAudioContext.toString = function(){
    return 'function OfflineAudioContext() { [native code] }'
}
Window.prototype.MediaEncryptedEvent = function MediaEncryptedEvent() {};
Window.prototype.MediaEncryptedEvent.toString = function(){
    return 'function MediaEncryptedEvent() { [native code] }'
}
Window.prototype.Path2D = function Path2D() {};
Window.prototype.Path2D.toString = function(){
    return 'function Path2D() { [native code] }'
}
Window.prototype.CDATASection = function CDATASection() {};
Window.prototype.CDATASection.toString = function(){
    return 'function CDATASection() { [native code] }'
}
Window.prototype.SpeechSynthesisUtterance = function SpeechSynthesisUtterance() {};
Window.prototype.SpeechSynthesisUtterance.toString = function(){
    return 'function SpeechSynthesisUtterance() { [native code] }'
}
Window.prototype.XMLHttpRequest = function XMLHttpRequest() {};
Window.prototype.XMLHttpRequest.toString = function(){
    return 'function XMLHttpRequest() { [native code] }'
}
Window.prototype.SourceBuffer = function SourceBuffer() {};
Window.prototype.SourceBuffer.toString = function(){
    return 'function SourceBuffer() { [native code] }'
}
Window.prototype.ScreenOrientation = function ScreenOrientation() {};
Window.prototype.ScreenOrientation.toString = function(){
    return 'function ScreenOrientation() { [native code] }'
}
Window.prototype.SVGGraphicsElement = function SVGGraphicsElement() {};
Window.prototype.SVGGraphicsElement.toString = function(){
    return 'function SVGGraphicsElement() { [native code] }'
}
Window.prototype.PerformancePaintTiming = function PerformancePaintTiming() {};
Window.prototype.PerformancePaintTiming.toString = function(){
    return 'function PerformancePaintTiming() { [native code] }'
}
Window.prototype.length = 0;
Window.prototype.localStorage = {};
Window.prototype.sessionStorage = {};
Window.prototype.outerHeight = 956;
Window.prototype.innerHeight = 150;
Window.prototype.outerWidth = 1680;
Window.prototype.innerWidth = 1680;
Window.prototype.onmessage = null;
Window.prototype.document = document;
window = new Window();

Object.defineProperties(window, {
    [Symbol.toStringTag]: {
        value: "window",
        configurable: true
    }
});



/////////////////////////////////
// screen检测
Screen = function(){};
Screen.prototype.availHeight = '956';
Screen.prototype.availLeft = '0';
Screen.prototype.availTop = '23';
Screen.prototype.availWidth = '1680';
screen = new Screen()

/////////////////////////////////
// Function.prototype.toString = function () {
//     console.log("Function.prototype.toString", this.name)
//     // debugger;
//     return "";
// }
/////////////////////////////////




// 其他检测
module = undefined;
__filename = undefined;
delete Buffer;
// delete process;
global.window = window;
global = undefined;
global = window;






/////////////////////////////////


window = vmProxy(window);
window.window = window;
window.self = window;
window.top = window;


/////////////////////////////////
var eval_ = window.eval;
window.eval = function(x){
    console.log("eval", x);
    return eval_(x);
}



// old_random = Math.random
// Math.random = function(){
//     console.log();
//     debugger;
//     return old_random();
// }

debugger;



