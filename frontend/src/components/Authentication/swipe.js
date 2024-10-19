var [initialX, initialY] = [null, null];

function startTouch(e) {
  try {
    initialX = e.touches[0].clientX;
    initialY = e.touches[0].clientY;
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
  try {
    var currentX = e.changedTouches[0].clientX;
  } catch (error) {
    console.error(error);
  }

  var diffX = initialX - currentX;

  if (Math.abs(diffX)) {
    // sliding horizontally
    if (diffX > 0) {
      return "left";
    } else {
      return "right";
    }
  }

  initialX = null;
  initialY = null;

  // e.preventDefault();
}
export { startTouch, moveTouch };
