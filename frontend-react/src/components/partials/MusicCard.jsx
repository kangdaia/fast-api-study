import { useState } from "react";
import fastAPIconn from "../../hooks/authenticate";
import "../../index.css";

function Track(params) {
    return (
        <div className="text-lg text-white flex flex-row align-center">
            <img className="rounded-lg" src={params.image[1]["#text"]} alt={params.image[1]["size"]}/>
            <div className="flex flex-col px-2 justify-center">
                <div className="font-bold">{params.name}</div>
                <p className="text-sm">{params.artist.name}</p>
            </div>
        </div>
    );
}

function TrackList(params) {
    
}