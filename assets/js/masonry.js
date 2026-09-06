$(document).ready(function () {
  // Init Masonry
  var $grid = $(".grid").masonry({
    horizontalOrder: true,
    itemSelector: ".grid-item",
    columnWidth: ".grid-sizer",
    percentPosition: true,
  });
  // Layout Masonry after each image loads
  $grid.imagesLoaded().progress(function () {
    $grid.masonry("layout");
  });
});
