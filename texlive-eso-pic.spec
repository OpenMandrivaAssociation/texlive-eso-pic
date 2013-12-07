# revision 31875
# category Package
# catalog-ctan /macros/latex/contrib/eso-pic
# catalog-date 2013-10-10 16:26:27 +0200
# catalog-license lppl1.2
# catalog-version 2.0d
Name:		texlive-eso-pic
Version:	2.0d
Release:	4
Summary:	Add picture commands (or backgrounds) to every page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eso-pic
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package adds one or more user commands to LaTeX's shipout
routine, which may be used to place the output at fixed
positions. The grid option may be used to find the correct
places.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
