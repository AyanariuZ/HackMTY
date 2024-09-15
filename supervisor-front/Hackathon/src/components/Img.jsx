import {Image} from "@nextui-org/react";

export default function App() {
  return (
    <div className="flex justify-center">
    <Image
      isBlurred
      src="http://127.0.0.1:5000/video_feed"
      alt="NextUI Album Cover"
      className="m-5 max-w-[800px] max-h-[400px] justify-center items-center justify-self-center"
    />
    </div>
    
  );
}
