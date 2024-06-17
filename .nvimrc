lua << EOF
local dap = require('dap')
dap.adapters.python = {
  type = 'executable';
  command = os.getenv("VIRTUAL_ENV") .. "/bin/python";
  args = { '-m', 'debugpy.adapter' };
}


dap.configurations.python = {
  {
    -- The first three options are required by nvim-dap
    type = 'python'; -- the type here established the link to the adapter definition: `dap.adapters.python`
    request = 'launch';
    name = "Launch file";
    cwd =  os.getenv("HOME") .. "/Codes/saa/";  --python is executed from this directory

    program = "${file}"; -- This configuration will launch the current file if used.
    pythonPath = function()
      -- debugpy supports launching an application with a different interpreter then the one used to launch debugpy itself.
      -- The code below looks for a `venv` or `.venv` folder in the current directly and uses the python within.
      -- You could adapt this - to for example use the `VIRTUAL_ENV` environment variable.
      local cwd = vim.fn.getcwd()
      if vim.fn.executable(cwd .. '/venv/bin/python') == 1 then
        return cwd .. '/venv/bin/python'
      elseif vim.fn.executable(cwd .. '/.venv/bin/python') == 1 then
        return cwd .. '/.venv/bin/python'
      else
        return  os.getenv("HOME") .. '/.virtualenvs/nvim/bin/python'
      end
    end;
  },
}
EOF


