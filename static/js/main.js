/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/blocks/modules/footer/footer.js":
/*!*********************************************!*\
  !*** ./src/blocks/modules/footer/footer.js ***!
  \*********************************************/
/***/ (() => {

/*if (document.referrer.indexOf(window.location.origin) != -1) {
  $('.modalCoocke').addClass("active");
  $('.modalCoocke_content').addClass("active");
  $('html, body').css({
    overflow: 'hidden'
  });
} else {
  console.log("from external site");
}*/
$('.modalCoockee_btn').on('click', function () {
  $('.modalCoocke').removeClass("active");
  $('.modalCoocke_content').removeClass("active");
  $('html, body').css({
    overflow: 'auto'
  });
});
$('.docsOpen').on('click', function (e) {
    e.preventDefault();
    let doc_id = $(this).attr('id');

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

  $.ajax({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        url:window.location.pathname,
        type:'POST',
        data: {id: doc_id},
        success:function(response){
            console.log(response);
            /*console.log(window.location.pathname);*/
            openModal(response);
        },
        error:function(){
            console.log('something went wrong here');
        },
    });

});

$(".cardTextOver").text(function(i, text) {
  if (text.length >= 510) {
    text = text.substring(0, 510);
    var lastIndex = text.lastIndexOf(" ");       // позиция последнего пробела
    text = text.substring(0, lastIndex); // обрезаем до последнего слова
  }
  
  $(this).text(text).append('<a href="#" class="cardLink">...читать далее</a>');
  
});

 function openModal(docs_data){
  $('#modalDocsName').text(docs_data.name);
  $('#modalDocsText').text(docs_data.text);

  $('.modalDocs').addClass("active");
  $('.modalDocs_content').addClass("active");
  $('html, body').css({
    overflow: 'hidden'
  });
 }

 $('.openNav').on('click', function () {
  $('.nav').toggleClass("active");
});


$('.docsClose').on('click', function () {
  $('.modalDocs').removeClass("active");
  $('.modalDocs_content').removeClass("active");
  $('html, body').css({
    overflow: 'auto'
  });
});
$('.langOpen').on('click', function () {
  $('.modalLAng').addClass("active");
  $('.modalLang_content').addClass("active");
  $('html, body').css({
    overflow: 'hidden'
  });
});
$('.langClose').on('click', function () {
  $('.modalLAng').removeClass("active");
  $('.modalLang_content').removeClass("active");
  $('html, body').css({
    overflow: 'auto'
  });
});
$('.userInfo').on('click', function () {
  $('.userInfoModal').addClass("active");
  $('.modalUserBg').addClass("active");
  $('html, body').css({
    overflow: 'hidden'
  });
});
$('.modalUserBg').on('click', function () {
  $('.userInfoModal').removeClass("active");
  $('.modalUserBg').removeClass("active");
  $('html, body').css({
    overflow: 'auto'
  });
});
$(".navListCont").on({
  mouseenter: function mouseenter() {
    $('.whiteBack').addClass("active");
    $('.navList').addClass("active");
  },
  mouseleave: function mouseleave() {
    $('.whiteBack').removeClass("active");
    $('.navList').removeClass("active");
  }
});
$(document).ready(function () {
  $('.slider__intro').slick({
    arrows: true,
    nextArrow: '<div class="arrow__slider right"><i class="fas fa-chevron-right"></i></div>',
    prevArrow: '<div class="arrow__slider left"><i class="fas fa-chevron-left"></i></div>',
    autoplay: true,
    slickPlay: false,
    responsive: [{
      settings: {
        draggable: true,
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }]
  });
  $('.slider__introNews').slick({
    arrows: true,
    nextArrow: '<div class="arrow__slider right"><i class="fas fa-chevron-right"></i></div>',
    prevArrow: '<div class="arrow__slider left"><i class="fas fa-chevron-left"></i></div>',
    autoplay: true,
    slickPlay: false,
    responsive: [{
      breakpoint: 1600,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1
      }
    }, {
      breakpoint: 1324,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1
      }
    }, {
    }, {
      breakpoint: 824,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }, {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }]
  });
});

/***/ }),

/***/ "./src/blocks/modules/header/header.js":
/*!*********************************************!*\
  !*** ./src/blocks/modules/header/header.js ***!
  \*********************************************/
/***/ (() => {



/***/ }),

/***/ "./src/js/import/components.js":
/*!*************************************!*\
  !*** ./src/js/import/components.js ***!
  \*************************************/
/***/ (() => {



/***/ }),

/***/ "./src/js/import/modules.js":
/*!**********************************!*\
  !*** ./src/js/import/modules.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _modules_header_header__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! %modules%/header/header */ "./src/blocks/modules/header/header.js");
/* harmony import */ var _modules_header_header__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_modules_header_header__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _modules_footer_footer__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! %modules%/footer/footer */ "./src/blocks/modules/footer/footer.js");
/* harmony import */ var _modules_footer_footer__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_modules_footer_footer__WEBPACK_IMPORTED_MODULE_1__);



/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be in strict mode.
(() => {
"use strict";
/*!*************************!*\
  !*** ./src/js/index.js ***!
  \*************************/
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _import_modules__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./import/modules */ "./src/js/import/modules.js");
/* harmony import */ var _import_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./import/components */ "./src/js/import/components.js");
/* harmony import */ var _import_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_import_components__WEBPACK_IMPORTED_MODULE_1__);


})();

/******/ })()
;
//# sourceMappingURL=main.js.map