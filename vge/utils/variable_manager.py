class VariableManager:
    def __init__(self):
        self.variables = {}
    
    def push(self, var_name, value):
        self.variables[var_name] = value
    
    def push_vs(self, var_name, vs):
        # Push variable system
        self.variables[var_name] = vs.copy()
    
    def get(self, var_name, default=None):
        return self.variables.get(var_name, default)
    
    def copy(self):
        vs_copy = VariableManager()
        for k, v in self.variables.items():
            vs_copy.push(k, v)
        
        return vs_copy
