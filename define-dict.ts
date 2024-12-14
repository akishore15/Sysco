import express from 'express';
import bodyParser from 'body-parser';
import { exec } from 'child_process';

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/execute', (req, res) => {
    const { command } = req.body;

    if (!command) {
        return res.status(400).send({ error: 'Command is required' });
    }

    exec(command, (error, stdout, stderr) => {
        if (error) {
            return res.status(500).send({ error: error.message });
        }

        if (stderr) {
            return res.status(500).send({ error: stderr });
        }

        res.send({ output: stdout });
    });
});

app.listen(port, () => {
    console.log(`Bash API running on http://localhost:${port}`);
});
