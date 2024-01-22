var [initialX, initialY] = [null, null];

function startTouch(e) {
  try {
    initialX = e.touches[0].clientX;
    initialY = e.touches[0].clientY;
    console.warn(initialX, initialY);
  } catch (error) {
    console.log(error);
  }
}
function moveTouch(e) {
  if (initialX === null) {
    return;
  }

  if (initialY === null) {
    return;
  }
  console.log(e);
  try {
    console.log(e.changedTouches);
    var currentX = e.changedTouches[0].clientX;
    var currentY = e.changedTouches[0].clientY;
  } catch (error) {
    console.error(error);
  }

  var diffX = initialX - currentX;
  var diffY = initialY - currentY;

  if (Math.abs(diffX)) {
    // sliding horizontally
    if (diffX > 0) {
      console.log("Swipe left");
      // swiped left
      // setLogin(true);
      return "left";
    } else {
      console.log("Swipe right");
      // swiped right
      // setLogin(false);
      return "right";
    }
  }

  initialX = null;
  initialY = null;

  // e.preventDefault();
}
export { startTouch, moveTouch };
