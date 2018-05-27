import { Component, OnInit } from '@angular/core';
import {GameService} from "../../services/game/game.service";

@Component({
  selector: 'app-trashure-menu',
  templateUrl: './trashure-menu.component.html',
  styleUrls: ['./trashure-menu.component.css']
})
export class TrashureMenuComponent implements OnInit {

  constructor(public game: GameService) { }

  ngOnInit() {
    this.playMusic();
  }

  startGame() {
    this.game.getGame().subscribe(x => this.game.startGame(x));
  }

  playMusic() {
    let audio = new Audio();
    audio.src = "assets/sounds/music.wav";
    audio.loop = true;
    audio.load();
    audio.play();
  }

}
