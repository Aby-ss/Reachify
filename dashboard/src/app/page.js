import Image from "next/image";

export default function Home() {
  return (
    <div className="flex flex-col gap-10 items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <h1 className="font-bold text-3xl tracking-[-.05em]">
        Insert your file below
      </h1>
      <p className="font-semibold text-xl tracking-[-.05em] w-[700px] text-center">
        Drag and drop your file containing the prospect detials in the area below. File type supported : csv excel files
      </p>

      <div className="border-dashed border-2 border-sky-500 w-[500px] h-[250px] p-[16px] rounded-md flex justify-center">
        <p className="font-bold text-lg tracking-[-.05em]">Drag n drop the files</p>
      </div>
    </div>
  );
}
