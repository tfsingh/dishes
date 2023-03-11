//basic react component skeleton
import React from "react";
import NavBar from "./NavBar";

function Summary() {
  return (
    <div>
      <div className="relative top-10 left-11 max-w-xl">
        A few quick notes &mdash; I initially wanted to work on building 3d
        visualizations from natural language but wasn&rsquo;t able to narrow the
        scope of my project in time. There were a lot of interesting avenues to
        explore (domain-specific visualizations, stable diffusion on 3d-objects,
        etc), and it all ended up being a little overwhelming. This is an area
        I&rsquo;ve been broadly interested in for a long time, so I&rsquo;ll
        certainly get around to building something in the space at some point.
        Also, the initial data on the homepage&rsquo;s chart isn&rsquo;t
        accurate (I used some random numbers to beef it up a little), but it is
        updated in real-time if the system is up and operational. <br />
        <br />
        <h1 className="font-bold">Problem Statement</h1>
        In terms of the problem I was trying to solve, it really is as simple as
        trying to figure out who left the dishes in the sink. We try to keep our
        place clean but the sink has always been an issue for us &mdash;
        it&rsquo;s difficult to take accountability for something you forgot
        about a week ago, so we&rsquo;d just get a larger and larger pile in
        there as time went on. The task of cleaning these usually fell on one
        fed-up person (thank you jshu, the favicon of this website), which I
        didn&rsquo;t like. The system I developed isn&rsquo;t perfect, but
        serves as a nice proof-of-concept for a more robust one that would be
        effective in solving this problem.
        <br />
        <br />
        <h1 className="font-bold">Technical Components</h1>
        Here&rsquo;s a rough architecture diagram, not because the architecture
        of this project is difficult to understand, but because they&rsquo;re
        pretty.
        <br />
        <img src="https://i.ibb.co/xH1RQnb/Screen-Shot-2023-03-10-at-11-43-13-PM.png" />
        In short, we take in frames from two camera feeds. If face(s) are
        detected and there&rsquo;s some new object in the sink, we wait
        &ldquo;wait_time&rdquo; seconds to allow that person to wash their dish.
        If it&rsquo;s still there after &ldquo;wait_time&rdquo; seconds, we
        increment that person&rsquo;s dish count in the database (google
        sheets), and send a SMS notification to (me, but could be the whole
        house), claiming that x person(s) left some dishes in the sink.
        <br />
        <br />
        Data collection for this project was just some basic OSINT &mdash;
        scrape my roommates' headshots from their LinkedIns and put them in a
        folder. We generate encodings from the face_recognition library in a
        small script, and then pass them into our detection file to identify
        similarities. <br />
        <br />
        The code for face and object detection was from some online tutorials
        and patchworked StackOverflow posts, as this was the toughest part to
        figure out. I did have to do quite a bit of work on the object detection
        front, testing two different mechanisms for object detection (OpenCV and
        Scikit-Image). This involved quite a bit of tweaking values to ensure I
        reached a sweet spot of sensitivity, as one can imagine that a sink
        isn&rsquo;t a particularly stagnant place. <br />
        <br />
        I wanted to make the system end-to-end (and a little overengineered,
        just for fun), so I had the Twilio API to send me notifications whenever
        a new dish was placed in the sink. It also updates the backend connected
        to the chart on the front page, so we can publicly shame whoever keeps
        doing this (boooo). <br />
        <br />
        Finally, I implemented the logic and flow of the system, bringing all
        the pieces together. The toughest aspect of the project was detecting
        whether a new dish was added (involves storing previous frames/a resting
        similarity score between each frame, which is ~90 instead of 100 btw),
        but I was able to get it working after some good old-fashioned printf
        debugging.
        <br />
        <br />
        <h1 className="font-bold">Limitations</h1>
        There are some limitations with the system &mdash; the most glaring
        being you need to be looking into the camera, which isn&rsquo;t the most
        reliable if we have a truly malicious actor in our midst (we don&rsquo;t
        though, we&rsquo;re just forgetful :)). There&rsquo;s no real logic to
        handle the case in which the lights are lower, but I was thinking of
        resetting the resting frame every 20 minutes to combat this. Finally,
        object detection just checks if the picture has changed &mdash; taking
        out the dish has the same effect, so a person cleaning up would get
        blamed for adding dishes! Not good, but again, this system is just a
        small proof-of-concept and all of these issues should be solvable with
        some tinkering.
        <br />
        <br />
        <h1 className="font-bold">Roadblocks</h1>
        Some roadblocks. Dependencies are a pain. OpenCV can be a pain to use,
        on a Mac (non-trivial to get multiple camera input streams). Object
        detection is tough! Face detection is tougher, but that&rsquo;s why
        libraries exist (thank you Adam Geitgey). <br />
        <br />
        <h1 className="font-bold">Takeaways</h1>
        Finally some takeaways. This project was quite fun &mdash; I got to
        build something from scratch, with some interconnected components and
        complexity to make it interesting. I learned quite a bit about some of
        the OSS tools out there in the computer vision space and liked them
        enough that I&rsquo;m looking to contribute to their communities (joined
        the OpenCV slack and reached out to some project mentors, hopefully, I
        can build something cool for them). I got exposure to some of the
        real-world issues with CV (lighting, camera quality, etc), and was
        surprised at how resilient/accurate the systems can be, especially at
        times when I didn&rsquo;t expect them to be. Very rewarding to make,
        with a somewhat useful result!
        <br />
        <br />
        <br />
      </div>
      <NavBar />
    </div>
  );
}

export default Summary;
