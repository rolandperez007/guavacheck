"use client";

interface Props {
  onClose?: () => void;
  onMinimize?: () => void;
  onMaximize?: () => void;
}

export default function WindowControls({ onClose, onMinimize, onMaximize }: Props) {
  return (
    <div className="flex items-center gap-2">
      <button
        onClick={onClose}
        className="h-3 w-3 rounded-full bg-red-500 transition hover:scale-110"
      />

      <button
        onClick={onMinimize}
        className="h-3 w-3 rounded-full bg-yellow-500 transition hover:scale-110"
      />

      <button
        onClick={onMaximize}
        className="h-3 w-3 rounded-full bg-green-500 transition hover:scale-110"
      />
    </div>
  );
}
