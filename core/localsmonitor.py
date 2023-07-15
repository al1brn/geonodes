import inspect
from pprint import pprint

# ====================================================================================================
# Capture locals in the stack and compare with previous state to get the created variables

class LocalsMonitor:
    def __init__(self):
        """ Monitor the creation of variables between construction and new_war()
        """
        
        # ----- Take a snaphot of the vars for each frame in the context
        
        self.snapshots = []
        for frame in reversed(inspect.stack()):
            self.snapshots.append((
                frame.function,
                [key for key in frame.frame.f_locals]
                ))
        
    # ----------------------------------------------------------------------------------------------------
    # Get the new variables created since the initialization
        
    def new_vars(self):
        
        # ----- Start from the bottom, last common frame in the stack
        
        calling_frame = None
        for i, frame in enumerate(reversed(inspect.stack())):
            if frame.function == self.snapshots[i][0]:
                calling_frame = frame
            else:
                snapshot = self.snapshots[i - 1]
                return {key: value for key, value in calling_frame.frame.f_locals.items() if not key in snapshot}
  
    # ----------------------------------------------------------------------------------------------------
    # Get the new variables created since the initialization

    def __str__(self):
        stack = [f"{i}: ({function} [{len(sn)}])" for i, (function, sn) in enumerate(self.snapshots)]
        return f"<LocalsMonitor, stack: " + ", ".join(stack) + ">"

    # ====================================================================================================
    # Dump the frames

    @staticmethod
    def dump_stack(title=""):
        
        frames = inspect.stack()
        
        print("="*60)
        print(f"{title} - LocalsMonitor dump frames ({len(frames)})")
        for i, frame in enumerate(frames):
            
            print(f"{i:3d} ({len(frame.frame.f_locals):3d})>", list(frame.frame.f_locals.keys()))
            code_context = frame.code_context
            if code_context is None:
                print("    | CC None\n")
            else:
                print(f"    | {code_context[0]:60s}")
                
            for k in dir(frame):
                if k.startswith('_'):
                    continue
                print(f"   frame.{k:12s} = {str(getattr(frame, k))[:30]}")
            print()
                
        print()

    # ====================================================================================================
    # Dump new variables

    @staticmethod
    def dump_new_vars(new_vars, title=""):
        
        print("="*60)
        print(f"{title} - LocalsMonitor dump new_vars ({len(new_vars)})")
        for k, v in new_vars.items():
            print(f"   {k:12s}: {str(v)[:30]}")
        print()
