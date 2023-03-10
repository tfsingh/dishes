//basic react component skeleton
import React from "react";

function Summary() {
  return (
    <div>
      <div className="relative top-10 left-11 max-w-xl">
        <p>
          Lorem Ipsum is simply dummy text of the printing and typesetting
          industry. Lorem Ipsum has been the industry's standard dummy text ever
          since the 1500s, when an unknown printer took a galley of type and
          scrambled it to make a type specimen book. It has survived not only
          five centuries, but also the leap into electronic typesetting,
          remaining essentially unchanged. It was popularised in the 1960s with
          the release of Letraset sheets containing Lorem Ipsum passages, and
          more recently with desktop publishing software like Aldus PageMaker
          including versions of Lorem Ipsum.
        </p>
      </div>
      <div className="absolute top-10 right-12">
        <a href="/">home</a>
        <br />
        <a>summary</a>
        <br />
        <a>video</a>
        <br />
        <a>other</a>
      </div>
    </div>
  );
}

export default Summary;
