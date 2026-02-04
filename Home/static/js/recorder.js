let recorder, audioChunks = [], isRecording = false;
let vrec, vchunks = [], isVRecording = false;

/* ---------- AUDIO TOGGLE ---------- */
function toggleAudio(){
  let audioBtn = document.getElementById("audioBtn");

  if(!isRecording){
    navigator.mediaDevices.getUserMedia({ audio: true }).then(stream=>{
      recorder = new MediaRecorder(stream, { mimeType: "audio/webm" });
      recorder.start();
      audioChunks = [];
      isRecording = true;

      audioBtn.textContent = "⏹";
      audioBtn.classList.add("recording");   // 🔴 GLOW ON

      recorder.ondataavailable = e => audioChunks.push(e.data);
    });
  } 
  else {
    recorder.stop();
    isRecording = false;

    audioBtn.textContent = "🎤";
    audioBtn.classList.remove("recording"); // ⚪ GLOW OFF

    recorder.onstop = () => {
      let blob = new Blob(audioChunks, { type: "audio/webm" });
      let url = URL.createObjectURL(blob);

      let audio = document.getElementById("preview");
      audio.src = url;
      audio.load();
      audio.play();

      let file = new File([blob], "recorded.webm", { type: "audio/webm" });
      let dt = new DataTransfer();
      dt.items.add(file);
      document.querySelector("input[name='audio']").files = dt.files;
    };
  }
}

/* ---------- VIDEO TOGGLE ---------- */
function toggleVideo(){
  if(!isVRecording){
    navigator.mediaDevices.getUserMedia({ video:true, audio:true }).then(stream=>{
      vrec = new MediaRecorder(stream, { mimeType: "video/webm" });
      vrec.start();
      vchunks=[];
      isVRecording=true;
      document.getElementById("videoBtn").textContent="⏹";
      vrec.ondataavailable=e=>vchunks.push(e.data);
    });
  } 
  else {
    vrec.stop();
    isVRecording=false;
    document.getElementById("videoBtn").textContent="📹";
    vrec.onstop=()=>{
      let blob=new Blob(vchunks,{type:"video/webm"});
      let url=URL.createObjectURL(blob);
      document.getElementById("vpreview").src=url;

      let file=new File([blob],"video.webm",{type:"video/webm"});
      let dt=new DataTransfer();
      dt.items.add(file);
      document.querySelector("input[name='video']").files = dt.files;
    }
  }
}
