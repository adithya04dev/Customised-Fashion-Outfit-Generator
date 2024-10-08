import broom from "./broom.png";
import send from "./send.png";
import chatIcon from "./chatIcon.png";
import "./App.css";
import { useEffect, useRef, useState } from "react";
import OutfitCard from "./OutfitCard";
import UserMessage from "./UserMessage";
import LoadingSpinner from "./Loader/Loader";

function App() {
  // var countMessages = 0;
  const [cntMsg, setCntMsg] = useState(0);
  const [outfitText, setOutfitText] = useState("");
  const messagesContainerRef = useRef(null);
  const [outfits, setOutfits] = useState([]);
  const [isSubmitDisabled, setIsSubmitDisabled] = useState(false);
  const [placeholderText, setPlaceholderText] = useState(
    "What outfit are you looking for?"
  );
  
  const [chatLog, setChatLog] = useState([]);

  useEffect(() => {
    window.addEventListener("beforeunload", clearChat);

    return () => {
      window.removeEventListener("beforeunload", clearChat);
    };
  }, []);

  useEffect(() => {
    if (chatLog.length) {
      console.log("Scroll to bottom ran", chatLog.length);

      messagesContainerRef.current?.scrollIntoView({
        behavior: "smooth",
        block: "end",
      });
    }
  }, [chatLog.length]);

  const clearChat = async () => {
    setChatLog([]);
    setOutfitText("");
    setIsSubmitDisabled(false);
    setCntMsg(0);
    setPlaceholderText("What outfit are you looking for?");
    try {
      //http://192.168.248.92:8122/reset_chat
      const response = await fetch("http://localhost:8122/reset_chat");
      if (response.ok) {
        console.log("Chat Cleared");
      } else {
        console.error("Error fetching data:", response.statusText);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleSubmit = async (event) => {
    let currCnt = cntMsg;
    currCnt += 1;
    console.log("curr cnt is ", currCnt);
    setIsSubmitDisabled(true);
    setPlaceholderText("Query in progress...");
    if (currCnt <= 1000) {
      event.preventDefault();
      const currText = outfitText;
      setOutfitText("");
      const currData = [
        {
          IsUser: true,
          UserPrompt: currText,
        },
        {
          IsUser: false,
          OutFits: [],
        },
      ];
      setChatLog((prevChats) => [...prevChats, ...currData]);
      const endpoint = "http://localhost:8122/get_outfit"; // Replace with your actual endpoint URL

      try {
        const response = await fetch(endpoint, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            credentials: "include",
          },
          body: JSON.stringify({ user_prompt: currText }),
        });

        if (response.status === 200) {
          // Handle successful response
          const data = await response.json();
          const currData = [
            {
              IsUser: false,
              OutFits: data.outfit,
            },
          ];
          setChatLog((prevChats) => {
            // Create a copy of the previous array
            const newChatLog = [...prevChats];

            // Remove the last item from the copy
            newChatLog.pop();

            // Add the new item (currData) to the end
            newChatLog.push(...currData);

            return newChatLog;
          });
          setIsSubmitDisabled(false);
          setOutfits(data.outfit);
          setCntMsg(currCnt);
          setPlaceholderText("What outfit are you looking for?");

          console.log("Outfit search successful!");
        } else {
          setIsSubmitDisabled(false);
          setChatLog((prevChats) => {
            // Create a copy of the previous array
            const newChatLog = [...prevChats];

            // Remove the last item from the copy
            newChatLog.pop();

            // Add the new item (currData) to the end

            return newChatLog;
          });
          setCntMsg(currCnt);
          setPlaceholderText(
            "I am sorry can't continue. I am still learning so I appreciate your understanding, Kindly Refresh"
          );
          console.error("Outfit search failed.");
        }
      } catch (error) {
        setIsSubmitDisabled(false);
        setCntMsg(currCnt);
        setPlaceholderText(
          "I am sorry can't continue. I am still learning so I appreciate your understanding, Kindly Refresh"
        );
        console.error("Error:", error);
      }
    } else {
      event.preventDefault();
      // const currText = outfitText;
      setOutfitText("");
      const endpoint = "http://localhost:8122/get_outfit";
      const currData = [
        {
          IsUser: false,
          OutFits: [],
        },
      ];
      setChatLog((prevChats) => [...prevChats, ...currData]);
      setIsSubmitDisabled(true);
      setPlaceholderText(
        "Limit Reached. Clear chat or refresh the page to continue!"
      );
    }
  };

  const handleOutfitTextChange = (event) => {
    setOutfitText(event.target.value);
  };
  const adjustTextareaHeight = (element) => {
    element.style.height = "auto";
    element.style.height = element.scrollHeight + "px";
  };

  const handleTextareaInput = (event) => {
    adjustTextareaHeight(event.target);
  };
  const handleTextAreaKeyDown = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      handleSubmit(event);
    }
  };
  return (
    <div ref={messagesContainerRef} className="App">
      <h2 className="WelcomeText">Lookify: A GenAI Outfit Generator!</h2>
      <hr className="HorizotalLine" />
      <div className="Container ">
        {chatLog.map((Obj, index) => (
          <>
            {Obj.IsUser ? (
              <div className="PrevSearchText">
                <UserMessage message={Obj.UserPrompt} />
              </div>
            ) : (
              <div className="ImageContainer">
                {Obj.OutFits && Obj.OutFits.length === 0 ? (
                  <>
                    {cntMsg >= 1000 ? (
                      <div className="Card2">
                        Sorry, You have reached the free tier chat message limit
                        of this conversation, Kindly clear the chat or upgrade
                        to a better plan!
                      </div>
                    ) : (
                      <div className="Card2">
                        {" "}
                        Waiting for the response, Hold Up!
                        {isSubmitDisabled ? <LoadingSpinner /> : null}
                      </div>
                    )}
                  </>
                ) : (
                  <div className="ImageContainer">
                    {Obj.OutFits &&
                      Obj.OutFits.map((outfit, index) => (
                        <div className="Card">
                          <OutfitCard outfit={outfit} id={index} />
                        </div>
                      ))}
                  </div>
                )}
              </div>
            )}
          </>
        ))}
      </div>

      <div className="QueryHolder">
        <button className="NewButton" onClick={clearChat}>
          <img src={broom} className="BroomImage" alt="Broom" />
        </button>
        <form>
          <div className="ChatContainer">
            <textarea
              className="PromptText"
              placeholder={placeholderText}
              value={outfitText}
              onChange={handleOutfitTextChange}
              id="fname"
              onInput={handleTextareaInput}
              name="fname"
              onKeyDown={handleTextAreaKeyDown}
              style={{ width: "100%", height: "auto" }}
              cols={1000}
              disabled={isSubmitDisabled}
              // rows={1}
            />
          </div>
        </form>
        <button className="NewButton" onClick={handleSubmit}>
          <img src={send} className="BroomImage" alt="Send Message" />
        </button>
      </div>
    </div>
  );
}

export default App;