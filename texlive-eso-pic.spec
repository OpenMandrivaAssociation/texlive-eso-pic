Name:		texlive-eso-pic
Version:	2.0c
Release:	1
Summary:	Add picture commands (or backgrounds) to every page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eso-pic
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Eso-pic is an extension of everyshi. Using everyshi's
\EveryShipout command, eso-pic adds one or more user commands
to LaTeX's shipout actions.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eso-pic/eso-pic.sty
%{_texmfdistdir}/tex/latex/eso-pic/showframe.sty
%doc %{_texmfdistdir}/doc/latex/eso-pic/eso-article-test.tex
%doc %{_texmfdistdir}/doc/latex/eso-pic/eso-ex1.tex
%doc %{_texmfdistdir}/doc/latex/eso-pic/eso-ex2.tex
%doc %{_texmfdistdir}/doc/latex/eso-pic/eso-ex3.tex
%doc %{_texmfdistdir}/doc/latex/eso-pic/eso-ex4.tex
%doc %{_texmfdistdir}/doc/latex/eso-pic/eso-ex5.tex
%doc %{_texmfdistdir}/doc/latex/eso-pic/eso-ex6.tex
%doc %{_texmfdistdir}/doc/latex/eso-pic/eso-memoir-test.tex
%doc %{_texmfdistdir}/doc/latex/eso-pic/eso-pic.pdf
#- source
%doc %{_texmfdistdir}/source/latex/eso-pic/eso-pic.dtx
%doc %{_texmfdistdir}/source/latex/eso-pic/eso-pic.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
