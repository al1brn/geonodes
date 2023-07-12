import inspect
from pprint import pprint

# ====================================================================================================
# Capture locals in the stack and compare with previous state to get the created variables

class LocalsMonitor:
    def __init__(self, f_call=lambda s: s.strip().startswith('with')):
        
        frames = inspect.stack()
        
        calling_frame = None
        self.locals_snapshot = []
        self.frame_depth = -1
        for frame in frames:
            
            self.frame_depth += 1
            
            if frame is None:
                continue
            
            code_context = frame.code_context
            if code_context is None:
                calling_frame = frame
                break
            
            if f_call(code_context[0]):
                calling_frame = frame
                break
                    
        if calling_frame is None:
            self.frame_depth = None
            return
        
        self.locals_snapshot = [key for key in calling_frame.frame.f_locals]
        
    def close(self):
        
        if self.frame_depth is None:
            return {}
        
        frame = inspect.stack()[self.frame_depth]
            
        return {key: value for key, value in frame.frame.f_locals.items() if not key in self.locals_snapshot}
    
    def __str__(self):
        return f"<LocalsMonitor, ok={self.frame_depth is not None}, snapshot:\n" + "\n   ".join(self.locals_snapshot) + "\n>\n"
    
    @staticmethod
    def dump_frames(frames):
        print("="*60)
        print(f"Dump frames: {len(frames)}")
        for i, frame in enumerate(frames):
            
            print(f"{i:3}> ", end = "")
            if frame is None:
                print("None")
                continue
            
            code_context = frame.code_context
            if code_context is None:
                print("CC None", frame.frame.f_locals)
                continue
            
            print(f"{code_context[0]:60s}")
        print()
