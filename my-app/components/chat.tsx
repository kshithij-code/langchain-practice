"use client"
import { MathJax } from "better-react-mathjax";
import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";

interface response {
    message: string
}

function Chat() {
    const [text, setText] = useState("");
    const [fetched, setFetched] = useState('');
    const [isreq, setIsReq] = useState(false);
    useEffect(() => {
        const foo = async () => {
            if (isreq) {
                const res = await fetch(`http://127.0.0.1:8000/?message="${text}"`)
                console.log(`http://127.0.0.1:8000/?message="${text}"`)
                const result: response = await res.json()
                setFetched(result.message);
                console.log(result.message)
                setIsReq(!isreq);
            }
        }
        foo()
    }, [setFetched, text, isreq]);
    return (
        <div>
            <input
                type="text"
                value={text}
                onChange={(e) => {
                    setText(e.target.value);
                }}
            />
            <button onClick={() => { setIsReq(!isreq) }}>submit</button>
            <MathJax inline dynamic>
                <br />
                <ReactMarkdown>
                    {fetched}
                </ReactMarkdown>
            </MathJax>
        </div>
    );
}

export default Chat;
