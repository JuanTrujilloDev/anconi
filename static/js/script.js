





$(function () {
    $(document).scroll(function () {
      var $nav = $(".navbarMain");
      var $logo = $(".logo");
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
      $nav.toggleClass('navbar-light', $(this).scrollTop() > $nav.height());
      $nav.removeClass('navbar-dark', $(this).scrollTop() > $nav.height());
      $nav.toggleClass('navbar-dark', $(this).scrollTop() < $nav.height());
      $logo.toggleClass('logo2', $(this).scrollTop() > $nav.height());
    });
  });


$(document).ready(function() {
  $(".link").click(function () {
      $(".link").removeClass("active");
      // $(".tab").addClass("active"); // instead of this do the below 
      $(this).addClass("active");   
  });
  });
/*   MARCAS SCRIPT */

window.jssor_1_slider_init = function() {

  var jssor_1_options = {
    $AutoPlay: 1,
    $Idle: 0,
    $SlideDuration: 3000,
    $SlideEasing: $Jease$.$Linear,
    $FillMode: 5,
    $PauseOnHover: 4,
    $SlideWidth: 300,
    $SlideSpacing: 30,
    $Align: 0
  };

  var jssor_1_slider = new $JssorSlider$("jssor_1", jssor_1_options);

  //make sure to clear margin of the slider container element
  jssor_1_slider.$Elmt.style.margin = "";

  /*#region responsive code begin*/

  /*
      parameters to scale jssor slider to fill parent container

      MAX_WIDTH
          prevent slider from scaling too wide
      MAX_HEIGHT
          prevent slider from scaling too high, default value is original height
      MAX_BLEEDING
          prevent slider from bleeding outside too much, default value is 1
          0: contain mode, allow up to 0% to bleed outside, the slider will be all inside parent container
          1: cover mode, allow up to 100% to bleed outside, the slider will cover full area of parent container
          0.1: flex mode, allow up to 10% to bleed outside, this is better way to make full window slider, especially for mobile devices
  */

  var MAX_WIDTH = 1920;
  var MAX_HEIGHT = 300;
  var MAX_BLEEDING = 0.128;

  function ScaleSlider() {
      var containerElement = jssor_1_slider.$Elmt.parentNode;
      var containerWidth = containerElement.clientWidth;

      if (containerWidth) {
          var originalWidth = jssor_1_slider.$OriginalWidth();
          var originalHeight = jssor_1_slider.$OriginalHeight();

          var containerHeight = containerElement.clientHeight || originalHeight;

          var expectedWidth = Math.min(MAX_WIDTH || containerWidth, containerWidth);
          var expectedHeight = Math.min(MAX_HEIGHT || containerHeight, containerHeight);

          //scale the slider to expected size
          jssor_1_slider.$ScaleSize(expectedWidth, expectedHeight, MAX_BLEEDING);

          //position slider at center in vertical orientation
          jssor_1_slider.$Elmt.style.top = ((containerHeight - expectedHeight) / 2) + "px";

          //position slider at center in horizontal orientation
          jssor_1_slider.$Elmt.style.left = ((containerWidth - expectedWidth) / 2) + "px";
      }
      else {
          window.setTimeout(ScaleSlider, 30);
      }
  }

  ScaleSlider();

  $Jssor$.$AddEvent(window, "load", ScaleSlider);
  $Jssor$.$AddEvent(window, "resize", ScaleSlider);
  $Jssor$.$AddEvent(window, "orientationchange", ScaleSlider);
  /*#endregion responsive code end*/
};


/* END MARCAS SCRIPT */



/* MAPA */
const iconFeature = new ol.Feature({
  geometry: new ol.geom.Point(ol.proj.fromLonLat([-75.29261, 2.93823])),
  name: 'Anconi',
});

var map = new ol.Map({
  interactions: ol.interaction.defaults({mouseWheelZoom:false}),
  target: 'map',
  controls: ol.control.defaults().extend([new ol.control.FullScreen()]),
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    }),
    new ol.layer.Vector({
      source: new ol.source.Vector({
        features: [iconFeature]
      }),
      style: new ol.style.Style({
        image: new ol.style.Icon({
          anchor: [0.5, 46],
          anchorXUnits: 'fraction',
          anchorYUnits: 'pixels',
          src: 'static/img/pointer.png'
        })
      })
    })
  ],
  view: new ol.View({
    center: ol.proj.fromLonLat([-75.29261, 2.93823]),
    zoom: 18
  })
});

/*   ENDMAPA */






