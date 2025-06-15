"use client"
import { useEffect, useState } from "react";

function Chat() {
    const [text, setText] = useState("");
    const [fetched, setFetched] = useState('<p>hi</p>');
    const [isreq, setIsReq] = useState(false);
    useEffect(() => {
        const foo = async () => {
            if (isreq) {
                let res = await fetch(`http://127.0.0.1:8000/?message=${text}`)
                res = await res.json()
                setFetched(res.message);
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
            <div dangerouslySetInnerHTML={{ __html: fetched }}></div>
        </div>
    );
}

export default Chat;
