%global tl_name eso-pic
%global tl_revision 79229

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0e
Release:	%{tl_revision}.1
Summary:	Add picture commands (or backgrounds) to every page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eso-pic
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds one or more user commands to LaTeX's shipout routine,
which may be used to place the output at fixed positions. The grid
option may be used to find the correct places.

